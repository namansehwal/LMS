<template>
  <div class="container mt-2">

    <!-- Recently Added Books -->
    <div class="row">
      <div class="col-lg-12 mb-1">
        <h2 class="text-center mb-6"><b><i><u>Recently Added Books</u></i></b></h2>
      </div>
      
      <div class="d-flex flex-wrap">
        <div v-for="book in recentlyAddedBooks" :key="book.id" class="col-lg-12 mb-4">
          <!-- Display recently added books as you did for Explore Library -->
          <div class="card-body recent-book-card">
            <h6 class="card-title book-title"><b>{{ book.name }}</b></h6>
            <p class="card-text book-info"><strong>Author:</strong> {{ book.author }}</p>
            <p class="card-text book-info"><strong>ISBN:</strong> {{ book.isbn }}</p>
            <p class="card-text book-info"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
            <div v-if="book.averageRating !== undefined" class="star-rating-container">
              <p class="card-text book-info"><strong>Rating:</strong></p>
              <div class="star-rating">
                <!-- <span v-if="book.averageRating === 0">&#9734;</span> -->
                <span v-for="star in 5" :class="{ filled: star <= book.averageRating }">&#9733;</span>
              </div>
            </div>
            <div v-else class="star-rating-container">
            <p class="card-text book-info"><strong>Rating:</strong></p>
            <div class="star-rating">
                <span v-for="star in 5">&#9733;</span>
            </div>
            </div>
            <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm request-btn">Request to Issue</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Top 5 Issued Books based on Rating -->
    <div class="row">
      <div class="col-lg-12 mb-1">
        <h2 class="text-center mb-6"><b><i><u>Top 5 Issued Books (Based on Rating)</u></i></b></h2>
      </div>

      <div class="d-flex flex-wrap">
        <div v-for="book in topRatedBooks" :key="book.id" class="col-lg-12 mb-4">
          <!-- Display top-rated books as you did for Explore Library -->
          <div class="card-body top-issued-book-card">
            <h6 class="card-title book-title"><b>{{ book.name }}</b></h6>
            <p class="card-text book-info"><strong>Author:</strong> {{ book.author }}</p>
            <p class="card-text book-info"><strong>ISBN:</strong> {{ book.isbn }}</p>
            <p class="card-text book-info"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
            <div v-if="book.averageRating !== undefined" class="star-rating-container">
              <p class="card-text book-info"><strong>Rating:</strong></p>
              <div class="star-rating">
                <!-- <span v-if="book.averageRating === 0">&#9734;</span> -->
                <span v-for="star in 5" :class="{ filled: star <= book.averageRating }">&#9733;</span>
              </div>
            </div>
            <div v-else class="star-rating-container">
            <p class="card-text book-info"><strong>Rating:</strong></p>
            <div class="star-rating">
                <span v-for="star in 5">&#9733;</span>
            </div>
            </div>
            <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm request-btn">Request to Issue</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Display Books -->
    <div class="row">
      <div class="col-lg-12 mb-1">
        <h2 class="text-center mb-6"><b><i><u>Explore Library...</u></i></b></h2>
      </div>

      <div v-for="section in filteredSections" :key="section.id" class="col-lg-12 mb-4">
        <div class="section-heading mb-1">
          <h3>{{ section.name }}</h3>
        </div>
        <div class="card-deck">
          <div v-for="book in filteredBooksBySection(section.id)" :key="book.id" class="card">
            <div class="card-body">
              <h6 class="card-title book-title"><b>{{ book.name }}</b></h6>
              <p class="card-text book-info"><strong>Author:</strong> {{ book.author }}</p>
              <p class="card-text book-info"><strong>ISBN:</strong> {{ book.isbn }}</p>
              <p class="card-text book-info"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
              <div v-if="book.averageRating !== undefined" class="star-rating-container">
                <p class="card-text book-info"><strong>Rating:</strong></p>
                <div class="star-rating">
                  <!-- <span v-if="book.averageRating === 0">&#9734;</span> -->
                  <span v-for="star in 5" :class="{ filled: star <= book.averageRating }">&#9733;</span>
                </div>
              </div>
              <div v-else class="star-rating-container">
              <p class="card-text book-info"><strong>Rating:</strong></p>
              <div class="star-rating">
                  <span v-for="star in 5">&#9733;</span>
              </div>
              </div>
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
      searchTerm: "",
    };
  },
  watch: {
    $route(to, from) {
      // Update the searchTerm when the route changes
      this.searchTerm = to.query.search || "";
    },
    searchTerm(newVal, oldVal) {
      // Update the route query when the searchTerm changes
      this.$router.replace({ query: { search: newVal } });
    },
  },
  computed: {
    recentlyAddedBooks() {
      // Implement logic to get recently added books (e.g., sort by creation date)
      const sortedBooks = this.books.slice().sort((a, b) => new Date(b.date_created) - new Date(a.date_created));
      return sortedBooks.slice(0, 5); // Display the top 5 recently added books
    },
    topRatedBooks() {
      // Implement logic to get top-rated books (e.g., sort by average rating)
      const ratedBooks = this.books.filter((book) => book.averageRating !== undefined);
      const sortedBooks = ratedBooks.slice().sort((a, b) => b.averageRating - a.averageRating);
      return sortedBooks.slice(0, 5); // Display the top 5 rated books
    },
    filteredBooks() {
      // Filter books based on the search term
      const searchTermLowerCase = this.searchTerm.toLowerCase();
      return this.books.filter((book) => {
        const lowerCaseName = book.name.toLowerCase();
        const lowerCaseAuthor = book.author.toLowerCase();

        return (
          lowerCaseName.includes(searchTermLowerCase) ||
          lowerCaseAuthor.includes(searchTermLowerCase) ||
          this.sections.find((section) => section.id === book.section_id).name.toLowerCase().includes(searchTermLowerCase)
        );
      });
    },
    filteredSections() {
      // Filter sections based on the search term
      const searchTermLowerCase = this.searchTerm.toLowerCase();
      return this.sections.filter((section) => section.name.toLowerCase().includes(searchTermLowerCase));
    },
  },
  methods: {
    async getAllBooks() {
      try {
        const response = await this.$axios.get('/book');
        this.books = response.data;
        // Fetch ratings for each book
        await this.fetchRatingsForBooks();
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
    async fetchRatingsForBooks() {
      // Fetch ratings for each book
      for (const book of this.books) {
        try {
          const response = await this.$axios.get(`/book/rating/${book.id}`);
          const ratingsData = response.data;
          
          // Check if ratings property exists in the API response
          if (Array.isArray(ratingsData.ratings)) {
            const ratings = ratingsData.ratings;
            console.log('Ratings for Book', book.id, ':', ratings);
          
            // Calculate average rating
          if (ratings.length > 0) {
            const averageRating = ratings.reduce((sum, rating) => sum + rating.rating_value, 0) / ratings.length;
            console.log('Average Rating for Book', book.id, ':', averageRating);
            
            // Add averageRating property to the book object
            book.averageRating = averageRating;
          } else {
            console.log('No Ratings for Book', book.id);
          }
        } else {
          console.log('No Ratings for Book', book.id);
        }
      } catch (error) {
        console.error(`Failed to fetch ratings for book ${book.id}:`, error);
      }
      }  
    },
    getBooksBySection(sectionId) {
      // Filter books by section
      return this.books.filter((book) => book.section_id === sectionId);
    },
    filteredBooksBySection(sectionId) {
      // Filter books by section based on the search term
      return this.filteredBooks.filter((book) => book.section_id === sectionId);
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
  mounted() {
    this.getAllBooks();
    this.getAllSections();
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


  .star-rating {
    color: #9e9ca7; /* Golden yellow color for stars */
  }

  .filled {
    color: #ff0008; /* Filled stars should also be golden yellow */
  }


  .star-rating-container {
    margin-bottom: 10px; /* Adjust the margin as needed */
    font-size: 15px;
    display: flex;
  }

  .recent-book-card {
  background: linear-gradient(45deg, #87CEEB, #4aa161); /* Gradient background */
  border: 1px solid #553403; /* White border */
  box-shadow: 0 2px 4px rgba(26, 183, 17, 0.1);
  min-width: 100px;
  margin-right: 10px;
  margin-left: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 10px;
  transition: transform 0.3s, box-shadow 0.3s;
  }

.top-issued-book-card {
  background: linear-gradient(45deg, #b6a753, #a33f83); /* Gradient background */
  border: 1px solid #760606; /* White border */
  box-shadow: 0 2px 4px rgba(67, 3, 3, 0.1);
  min-width: 100px;
  margin-right: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  margin-top: 10px;
  border-radius: 10px;
  transition: transform 0.3s, box-shadow 0.3s;
}

</style>
