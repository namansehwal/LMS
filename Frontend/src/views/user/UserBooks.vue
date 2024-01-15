<template>
    <div class="container mt-5">
      <!-- Display Books -->
      <div class="row">
        <div class="col-lg-12 mb-4">
          <h2 class="text-center mb-4">Explore Our Library</h2>
        </div>
  
        <div v-for="section in sections" :key="section.id" class="col-lg-12 mb-4">
          <div class="section-heading mb-3">
            <h3>{{ section.name }}</h3>
          </div>
          <div class="card-deck">
            <div v-for="book in getBooksBySection(section.id)" :key="book.id" class="card">
              <div class="card-body">
                <h5 class="card-title">{{ book.name }}</h5>
                <p class="card-text">{{ book.author }}</p>
                <p class="card-text"><strong>ISBN:</strong> {{ book.isbn }}</p>
                <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm">Request to Issue</button>
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
    background-color: #343a40;
    color: white;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
  }
  
  /* Styles for card deck and cards */
  .card-deck {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    scrollbar-width: thin;
  }
  
  .card {
    min-width: 200px;
    margin-right: 10px;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    transition: transform 0.3s;
  }
  
  .card:hover {
    transform: scale(1.05);
  }
  
  /* Styles for buttons */
  .btn-primary {
    background-color: #007bff;
    border-color: #007bff;
  }
  
  .btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
  }
  </style>
  