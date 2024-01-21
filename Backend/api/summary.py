from flask_restful import Resource
from flask import jsonify
from model import db, User, Section, Book, BookRequest, AccessLog, Rating
from sqlalchemy import func
from datetime import datetime, timedelta
import random

class SummaryAPI(Resource):
    def get(self):
        try:
            result = {}
            # Calculate total users
            total_users = User.query.count()

            # Calculate total books
            total_books = Book.query.count()
            unavailable = Book.query.filter(Book.id < 1).count()

            # Calculate total sections
            total_sections = Section.query.count()

            # Calculate total book requests
            total_book_requests = BookRequest.query.count()

            # Calculate total access logs
            total_access_logs = AccessLog.query.count()

            # Calculate total ratings
            total_ratings = Rating.query.count()

            # Calculate total overdue books
            overdue_books = AccessLog.query.filter(AccessLog.status == "Issued", AccessLog.due_date < datetime.now()).count()

            #total penalty
            total_penalty = int(round(overdue_books * 25))
            
            # Calculate total issued books
            total_issued_books = AccessLog.query.filter(AccessLog.status == "Issued").count()

            # Calculate total returned books
            total_returned_books = AccessLog.query.filter(AccessLog.status == "Returned").count()

            # Calculate total book copies
            total_book_copies = func.sum(Book.number_of_pages).label("total_pages")
            result = (
                db.session.query(total_book_copies)
                .filter(Book.id.in_(AccessLog.query.filter(AccessLog.status == "Issued").with_entities(AccessLog.book_id)))
                .first()
            )
            total_pages = result.total_pages if result else 0

            # Calculate section-wise book count
            section_wise_book_count = {}
            sections = Section.query.all()
            for section in sections:
                book_count = Book.query.filter_by(section_id=section.id).count()
                section_wise_book_count[section.name] = book_count

            # Calculate top-rated books (Assuming top 5 based on rating_value)
            top_books_query = (
                db.session.query(Book, func.avg(Rating.rating_value).label("avg_rating"))
                .join(Rating, Book.id == Rating.book_id)
                .group_by(Book.id)
                .order_by(func.avg(Rating.rating_value).desc())
                .limit(5)
            )
            top_books_list = top_books_query.all()
            random.shuffle(top_books_list)
            top_books = [
                {
                    "book_name": book.name,
                    "average_rating": avg_rating,
                }
                for book, avg_rating in top_books_list
            ]

            # Prepare the summary data
            result = {
                "total_users": total_users,
                "total_books": total_books,
                "unavailable": unavailable,
                "total_sections": total_sections,
                "total_book_requests": total_book_requests,
                "total_access_logs": total_access_logs,
                "total_ratings": total_ratings,
                "overdue_books": overdue_books,
                "total_penalty": total_penalty,
                "total_issued_books": total_issued_books,
                "total_returned_books": total_returned_books,
                "total_book_copies": total_pages,
                "section_wise_book_count": section_wise_book_count,
                "top_books": top_books,
            }

            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500