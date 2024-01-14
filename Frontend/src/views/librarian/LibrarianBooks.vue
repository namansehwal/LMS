<template>
  <div class="container mt-5">

    <!-- Add Book Form -->
    <div class="card mt-4 mb-4">
      <div class="card-header bg-primary text-white">
        Add Book
      </div>
      <div class="card-body">
        <form @submit.prevent="addBook">
          <div class="mb-3">
            <label for="bookName" class="form-label">Book Name</label>
            <input v-model="newBook.name" type="text" class="form-control" id="bookName" required>
          </div>
          <div class="mb-3">
            <label for="content" class="form-label">Content</label>
            <textarea v-model="newBook.content" class="form-control" id="content" rows="1" required></textarea>
          </div>
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="isbn" class="form-label">ISBN</label>
              <input v-model="newBook.isbn" type="text" class="form-control" id="isbn" required>
            </div>
            <div class="col-md-6 mb-3">
              <label for="author" class="form-label">Author</label>
              <input v-model="newBook.author" type="text" class="form-control" id="author" required>
            </div>
          </div>
          <div class="mb-3">
            <label for="sectionId" class="form-label">Section ID</label>
            <input v-model="newBook.section_id" type="number" class="form-control" id="sectionId" required>
          </div>
          <button type="submit" class="btn btn-primary">Add Book</button>
        </form>
      </div>
    </div>

    <!-- Display Books -->
    <div class="card mt-4 mb-4">
      <div class="card-header bg-info text-white">
        All Books
      </div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Content</th>
              <th>ISBN</th>
              <th>Author</th>
              <th>Date Issued</th>
              <th>Return Date</th>
              <th>Section ID</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in books" :key="book.id">
              <td>{{ book.id }}</td>
              <td>{{ book.name }}</td>
              <td>{{ book.content }}</td>
              <td>{{ book.isbn }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.date_issued }}</td>
              <td>{{ book.return_date }}</td>
              <td>{{ book.section_id }}</td>
              <td>
                <button @click="editBook(book)" class="btn btn-warning btn-sm mr-2">Edit</button>
                <button @click="deleteBook(book.id)" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  
    <!-- Edit Book Form -->
    <div v-if="editingBook" class="card mt-4 mb-4">
      <div class="card-header bg-success text-white">
        Edit Book
      </div>
      <div class="card-body">
        <form @submit.prevent="updateBook">
          <div class="mb-3">
            <label for="editBookName" class="form-label">Book Name</label>
            <input v-model="editingBook.name" type="text" class="form-control" id="editBookName" required>
          </div>
          <div class="mb-3">
            <label for="editContent" class="form-label">Content</label>
            <textarea v-model="editingBook.content" class="form-control" id="editContent" rows="1" required></textarea>
          </div>
            <div class="row">
            <div class="col-md-6 mb-3">
              <label for="editISBN" class="form-label">ISBN</label>
              <input v-model="editingBook.isbn" type="text" class="form-control" id="editISBN" required>
            </div>
            <div class="col-md-6 mb-3">
              <label for="editAuthor" class="form-label">Author</label>
              <input v-model="editingBook.author" type="text" class="form-control" id="editAuthor" required>
            </div>
          </div>
          <div class="mb-3">
            <label for="editSectionId" class="form-label">Section ID</label>
            <input v-model="editingBook.section_id" type="number" class="form-control" id="editSectionId" required>
          </div>
          <button type="submit" class="btn btn-success">Update Book</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newBook: {
        name: '',
        content: '',
        isbn: '',
        author: '',
        section_id: ''
      },
      books: [],
      editingBook: null
    };
  },
  mounted() {
    this.getAllBooks();
  },
  methods: {
    async addBook() {
      try {
        const response = await this.$axios.post('/book', this.newBook);
        this.getAllBooks();
        // Clear the form after adding the book
        this.newBook = {
          name: '',
          content: '',
          isbn: '',
          author: '',
          section_id: ''
        };
      } catch (error) {
        console.error('Add Book failed:', error);
      }
    },
    async getAllBooks() {
      try {
        const response = await this.$axios.get('/book');
        this.books = response.data;
      } catch (error) {
        console.error('Get Books failed:', error);
      }
    },
    editBook(book) {
      this.editingBook = { ...book };
    },
    async updateBook() {
      try {
        await this.$axios.put(`/book`, {
          id: this.editingBook.id,
          name: this.editingBook.name,
          content: this.editingBook.content,
          isbn: this.editingBook.isbn,
          author: this.editingBook.author,
          section_id: this.editingBook.section_id
        });

        this.editingBook = null;
        this.getAllBooks();
      } catch (error) {
        console.error('Update Book failed:', error);
      }
    },
    async deleteBook(bookId) {
      try {
        await this.$axios.delete(`/book`, { data: { id: bookId } });
        this.getAllBooks();
      } catch (error) {
        console.error('Delete Book failed:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Center the card in the middle of the page */
.container {
display: flex;
justify-content: center;
align-items: left;
min-height: 50vh;
}

/* Add some spacing to the buttons for better readability */
.btn {
margin-right: 5px;
}

/* Make the card header text bold */
.card-header {
font-weight: bold;
}

/* Custom styles for the form headers */
.card-header.bg-primary,
.card-header.bg-info,
.card-header.bg-success {
text-align: center;
font-size: 1.2rem;
}

/* Style table header */
.table thead th {
background-color: #343a40;
color: white;
}

/* Style alternating rows in the table */
.table-striped tbody tr:nth-child(odd) {
background-color: #f8f9fa;
}

/* Hover effect for table rows */
.table-hover tbody tr:hover {
background-color: #e2e6ea;
}
</style>
