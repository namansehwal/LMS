<template>
  <div class="container mt-4">

    <!-- Display the search results -->
    <div class="row">
      <div class="col-lg-12 mb-4">
        <h2 class="text-center mb-4"><u>Search Results</u></h2>
      </div>

      <div class="d-flex flex-wrap justify-content-center">
        <div v-if="searchResults.length > 0" class="col-lg-6 mb-4">
          <div v-for="book in searchResults" :key="book.id" class="card search-result-card mb-3">
            <img :src="book.image_url" class="card-img-top img-fluid book-image" alt="Book Image">
            <div class="card-body">
              <h5 class="card-title"><b>{{ book.name }}</b></h5>
              <p class="card-text"><strong>Author:</strong> {{ book.author }}</p>
              <p class="card-text"><strong>Section:</strong> {{ book.section }}</p>
              <div v-if="book.averageRating !== undefined" class="star-rating-container">
                <p class="card-text"><strong>Rating:</strong></p>
                <div class="star-rating">
                  <span v-for="star in 5" :class="{ filled: star <= book.averageRating }">&#9733;</span>
                </div>
              </div>
              <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm request-btn">Request to
                Issue</button>
            </div>
          </div>
        </div>
        <div v-else class="col-lg-12 mb-4">
          <p class="text-center">No results found.</p>
        </div>
      </div>
    </div>

    <!-- Recently Added Books -->
    <div class="col-lg-12 mb-2">
      <h2 class="text-center mb-4"><u>Recently Added Books</u></h2>
    </div>
    <div class="row">


      <div class="d-flex flex-wrap ">
        <div v-for="book in recentlyAddedBooks" :key="book.id" class="col-lg-2 m-1">
          <div class="card-body d-flex flex-column border ">
            <img :src="book.image_url" class="card-img-top book-image" alt="Book Image">
            <div class="card-body">
              <h5 class="card-title"><b>{{ book.name }}</b></h5>
              <p class="card-text"><strong>Author:</strong> {{ book.author }}</p>
              <p class="card-text"><strong>ISBN:</strong> {{ book.isbn }}</p>
              <p class="card-text"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
              <div v-if="book.averageRating !== undefined" class="star-rating-container">
                <p class="card-text"><strong>Rating:</strong></p>
                <div class="star-rating">
                  <span v-for="star in 5" :class="{ filled: star <= book.averageRating }">&#9733;</span>
                </div>
              </div>
              <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm request-btn">Request to
                Issue</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Top 5 Issued Books based on Rating -->
    <div class="row">
      <div class="col-lg-12 mb-4">
        <h2 class="text-center mb-4"><u>Top 5 Issued Books (Based on Rating)</u></h2>
      </div>

      <div class="d-flex flex-wrap justify-content-center">
        <div v-for="book in topRatedBooks" :key="book.id" class="col-lg-4 mb-4">
          <div class="card top-issued-book-card">
            <img :src="book.image_url" class="card-img-top img-fluid book-image" alt="Book Image">
            <div class="card-body">
              <h5 class="card-title"><b>{{ book.name }}</b></h5>
              <p class="card-text"><strong>Author:</strong> {{ book.author }}</p>
              <p class="card-text"><strong>ISBN:</strong> {{ book.isbn }}</p>
              <p class="card-text"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
              <div v-if="book.averageRating !== undefined" class="star-rating-container">
                <p class="card-text"><strong>Rating:</strong></p>
                <div class="star-rating">
                  <span v-for="star in 5" :class="{ filled: star <= book.averageRating }">&#9733;</span>
                </div>
              </div>
              <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm request-btn">Request to
                Issue</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Display Books -->
    <div class="row">
      <div class="col-lg-12 mb-4">
        <h2 class="text-center mb-4"><u>Explore Library...</u></h2>
      </div>

      <div v-for="section in sections" :key="section.id" class="col-lg-4 mb-4">
        <div class="section-heading mb-3">
          <h3>{{ section.name }}</h3>
        </div>
        <div class="card-deck">
          <div v-for="book in getBooksBySection(section.id)" :key="book.id" class="card mb-3">
            <img :src="book.image_url" class="card-img-top img-fluid book-image" alt="Book Image">
            <div class="card-body">
              <h5 class="card-title"><b>{{ book.name }}</b></h5>
              <p class="card-text"><strong>Author:</strong> {{ book.author }}</p>
              <p class="card-text"><strong>ISBN:</strong> {{ book.isbn }}</p>
              <p class="card-text"><strong>Pages:</strong> {{ book.number_of_pages }}</p>
              <div v-if="book.averageRating !== undefined" class="star-rating-container">
                <p class="card-text"><strong>Rating:</strong></p>
                <div class="star-rating">
                  <span v-for="star in 5" :class="{ filled: star <= book.averageRating }">&#9733;</span>
                </div>
              </div>
              <button @click="requestToIssue(book.id)" class="btn btn-primary btn-sm request-btn">Request to
                Issue</button>
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

<style>
.book-image {
  height: 325px;
}

.card-body {
  padding: 15px;
}
</style>
