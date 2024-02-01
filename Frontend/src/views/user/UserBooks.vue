<template>
  <div class="container mt-2">

    <!-- Display the search results -->
    <div class="row">
      <div class="col-lg-12 mb-1">
        <h2 class="text-center mb-6"><b><i><u>Search Results</u></i></b></h2>
      </div>

      <div class="d-flex flex-wrap">
        <div v-if="searchResults.length > 0" class="col-lg-12 mb-4">
          <div v-for="book in searchResults" :key="book.id" class="search-result-card">
            <div class="card-body">
              <p class="card-text book-info">
                <strong>Book:</strong> {{ book.name }}
              </p>
              <p class="card-text book-info">
                <strong>Author:</strong> {{ book.author }}
              </p>
              <p class="card-text book-info">
                <strong>Section:</strong> {{ book.section }}
              </p>
              <div v-if="book.averageRating !== undefined" class="star-rating-container">
                <p class="card-text book-info"><strong>Rating:</strong></p>
                <div class="star-rating">
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
        <div v-else class="col-lg-12 mb-4">
          <p class="text-center">No results found.</p>
        </div>
      </div>
    </div>

    <!-- Recently Added Books -->
    <div class="row">
      <div class="col-lg-12 mb-1">
        <h2 class="text-center mb-6"><b><i><u>Recently Added Books</u></i></b></h2>
      </div>
      
      <div class="d-flex flex-wrap">
        <div v-for="book in recentlyAddedBooks" :key="book.id" class="col-lg-12 mb-4">
          <div class="card-body recent-book-card">
            <h6 class="card-title book-title"><b>{{ book.name }}</b></h6>
            <p class="card-text book-info"><strong>Author:</strong> {{ book.author }}</p>
            <p class="card-text book-info"><strong>ISBN:</strong> {{ book.isbn }}</p>
            <p class="card-text book-info"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
            <div v-if="book.averageRating !== undefined" class="star-rating-container">
              <p class="card-text book-info"><strong>Rating:</strong></p>
              <div class="star-rating">
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
          <div class="card-body top-issued-book-card">
            <h6 class="card-title book-title"><b>{{ book.name }}</b></h6>
            <p class="card-text book-info"><strong>Author:</strong> {{ book.author }}</p>
            <p class="card-text book-info"><strong>ISBN:</strong> {{ book.isbn }}</p>
            <p class="card-text book-info"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
            <div v-if="book.averageRating !== undefined" class="star-rating-container">
              <p class="card-text book-info"><strong>Rating:</strong></p>
              <div class="star-rating">
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
              <p class="card-text book-info"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
              <div v-if="book.averageRating !== undefined" class="star-rating-container">
                <p class="card-text book-info"><strong>Rating:</strong></p>
                <div class="star-rating">
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
import { ref, computed } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const searchResults = computed(() => store.state.searchResults);
    const searchType = ref('');
    const searchQuery = ref('');

    const setSearchType = (type) => {
      searchType.value = type;
    };

    const searchBooks = async () => {
      console.log('Search books method called');
      try {
        setSearchType(determineSearchType()); // Update searchType
        await store.dispatch('searchBooks', searchQuery.value);
        console.log('Search results:', searchResults.value);
        // searchResults.value.forEach(book => console.log('Book Section:', book.section));
      } catch (error) {
        console.error('Error searching books:', error);
      }
    };

    return {
      searchResults,
      searchType,
      setSearchType,
      searchQuery,
      searchBooks,
    };
  },
  data() {
    return {
      books: [],
      sections: [],
    };
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
        console.error('Error fetching sections:', error);
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
    async requestToIssue(bookId) {
      // Add your logic for requesting to issue a book
      try {
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
    background-color: #96c5b0; 
    color: #7107b7c4; 
    padding: 5px;
    border-radius: 10px;
    margin-bottom: 10px;
    border: 3px solid #3d7e61;
    box-shadow: 0 2px 4px rgba(5, 5, 194, 0.1); 
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
    box-shadow: 0 2px 4px rgba(31, 3, 3, 0.1); 
  }

  .card-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: left;
  padding: 5px; 
  line-height: 0.1;
  background-color: #e7c8c8; 
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(17, 1, 33, 0.1); 
 }
  .card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
  }

  /* Styling for the book title */
.book-title {
  font-size: 1.2rem; 
  color: #34061e; 
  margin-bottom: 10px; 
  text-align: center
}

/* Styling for book information (author and ISBN) */
.book-info {
  color: #6d4a0a; 
  margin-bottom: 20px;
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
    color: #9e9ca7; 
  }

  .filled {
    color: #ff0008; 
  }


  .star-rating-container {
    margin-bottom: 10px; 
    font-size: 15px;
    display: flex;
  }

  .recent-book-card {
  background: linear-gradient(45deg, #87CEEB, #4aa161); 
  border: 1px solid #553403; 
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
  background: linear-gradient(45deg, #b6a753, #a33f83); 
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

.search-result-card {
  background: #e7c8c8; 
  border: 1px solid #6418bb; 
  padding-top: 15px;
  margin-right: 10px;
  margin-left: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}


</style>
