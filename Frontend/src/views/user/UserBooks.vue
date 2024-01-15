<template>
    <div class="container mt-2">
      <!-- Display Books -->
      <div class="row">
        <div class="col-lg-12 mb-1">
          <h2 class="text-center mb-6"><b><i><u>Explore Your Library...</u></i></b></h2>
        </div>
  
        <div v-for="section in sections" :key="section.id" class="col-lg-12 mb-4">
          <div class="section-heading mb-1">
            <h3>{{ section.name }}</h3>
          </div>
          <div class="card-deck">
            <div v-for="book in getBooksBySection(section.id)" :key="book.id" class="card">
              <div class="card-body">
                <h6 class="card-title book-title"><b>{{ book.name }}</b></h6>
                <p class="card-text book-info"><strong>Author:</strong> {{ book.author }}</p>
                <p class="card-text book-info"><strong>ISBN:</strong> {{ book.isbn }}</p>
                <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm request-btn">Request to Issue</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        books: [],
        sections: [],
      };
    },
    mounted() {
      this.getAllBooks();
      this.getAllSections();
    },
    computed: {
      uniqueCategories() {
        const categories = new Set(this.books.map((book) => book.category));
        return Array.from(categories);
      },
    },
    methods: {
      async getAllBooks() {
        try {
          const response = await this.$axios.get('/book');
          this.books = response.data;
        } catch (error) {
          console.error('Get Books failed:', error);
        }
      },
      async getAllSections() {
        try {
          const response = await this.$axios.get('/section');
          this.sections = response.data;
        } catch (error) {
          console.error('Get Sections failed:', error);
        }
      },
      getBooksBySection(sectionId) {
        // Filter books by section
        return this.books.filter((book) => book.section_id === sectionId);
      },
      async requestToIssue(bookId) {
        // Add your logic for requesting to issue a book
        try {
          // You might want to send a request to the server to handle the book issuance request
          // make a POST request to /book/request with the book ID and user ID
          const response = await this.$axios.post('/book/request', {
            book_id: bookId,
            user_id: localStorage.getItem('user_id'),
          });
          alert(response.data.message);
        } catch (error) {
          console.error('Request to Issue failed:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Styles for section heading */
  .section-heading {
    background-color: #96c5b0; /* Darker gray color */
    color: #7107b7c4; /* White text */
    padding: 5px;
    border-radius: 10px;
    margin-bottom: 10px;
    border: 3px solid #3d7e61;
    box-shadow: 0 2px 4px rgba(5, 5, 194, 0.1); /* Subtle box-shadow */
  }

  /* Styles for card deck and cards */
  .card-deck {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    scrollbar-width: thin;
    border: 2px solid #62cca5;
    border-radius: 20px
  }

  .card {
    min-width: 100px;
    margin-right: 10px;
    margin-left: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
    border: 1px solid #456789;
    border-radius: 10px;
    transition: transform 0.3s, box-shadow 0.3s;
    box-shadow: 0 2px 4px rgba(31, 3, 3, 0.1); /* Subtle box-shadow */
  }

  .card-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: left;
  padding: 5px; /* Adjust padding based on your design */
  line-height: 0.1;
  background-color: #e7c8c8; /* Light background color */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 4px 8px rgba(17, 1, 33, 0.1); /* Subtle box-shadow */
 }
  .card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Elevated box-shadow on hover */
  }

  /* Styling for the book title */
.book-title {
  font-size: 1.2rem; /* Larger font size */
  color: #34061e; /* Dark text color */
  margin-bottom: 10px; /* Spacing at the bottom */
  text-align: center
}

/* Styling for book information (author and ISBN) */
.book-info {
  color: #6d4a0a; /* Slightly muted text color */
  margin-bottom: 20px; /* Spacing at the bottom */
}

  /* Styles for buttons */
  .btn-primary {
    background-color: #d07dbf;
    border-color: #302303;
    color: #0e0d0c;
    border-radius: 70px;
    transition: background-color 0.3s;
  }

  .btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
  }
</style>
