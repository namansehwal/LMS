<template>
  <div class="m-3">
    <!-- Recently Added Books Section -->
    <div>
      <div v-if="hasQueryParams">
        <center>
          <h1 class="mt-4">{{ search_message }}</h1>
        </center>
      </div>
      <div v-if="recentlyAdded.length && !hasQueryParams" class="mb-5">
        <h3>Recently Added Books</h3>
        <div class="row">
          <div v-for="book in recentlyAdded" :key="book.id" class="col-lg-2">
            <div class="card h-100">
              <img :src="book.image_url" class="card-img-top book-image" alt="Book Image" />
              <div class="card-body d-flex flex-column">
                <h5 class="card-title">{{ book.name }}</h5>

                <p class="card-text">
                  <span class="author-label">Author:</span> {{ book.author }}
                </p>
                <p class="card-text">
                  <span class="price-label">Price:</span> ₹{{ book.price }}
                </p>
                <p class="card-text">
                  <label for="section">Section:</label> {{ book.section }}
                </p>
                <!-- Issue Button -->
                <div class="mt-auto">
                  <button class="btn btn-success mt-2" @click="issueBook(book)">Issue</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section-wise Books Section -->
    <div v-for="(section, sectionId) in sections" :key="sectionId">
      <hr />
      <h3>{{ section.name }}</h3>
      <div class="row">
        <div v-for="book in section.books" :key="book.id" class="col-lg-2 col-md-4 col-sm-6 mb-4">
          <div class="card h-100">
            <img :src="book.image_url" class="card-img-top book-image" alt="Book Image" />
            <div class="card-body d-flex flex-column">
              <h5 class="card-title">{{ book.name }}</h5>
              <div>
                <p class="card-text">
                  <span class="author-label">Author:</span> {{ book.author }}
                </p>
                <p class="card-text">
                  <span class="price-label">Price:</span> ₹{{ book.price }}
                </p>
                <!-- Issue Button -->
                <div class="mt-auto">
                  <button class="btn btn-success mt-2" @click="issueBook(book)">Issue</button>
                </div>
              </div>
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
      sections: {},
      recentlyAdded: [],
      queryParams: this.$route.query,
      search_message: ''
    }
  },

  mounted() {
    this.getBooks()
  },
  computed: {
    hasQueryParams() {
      // if no book is found
      if (Object.keys(this.sections).length == 0) {
        this.search_message = 'No book found'
      } else {
        // Handle search message based on query parameters
      }

      return Object.keys(this.queryParams).length > 0;

    },
  },
  methods: {
    async getBooks() {
      try {
        const bookResponse = await this.$axios.get('/book');
        const sectionResponse = await this.$axios.get('/section');

        this.processBooks(bookResponse.data, sectionResponse.data, this.$route.query)
        this.sortRecentlyAdded(bookResponse.data)
      } catch (error) {
        console.error('Error fetching books:', error)
      }
    },
    sortRecentlyAdded(books) {
      // Sort and limit to 5 recently added books that is last 5 books and convert book object to array
      this.recentlyAdded = Object.values(books)
        .sort((a, b) => b.id - a.id)
        .slice(0, 5)
    },
    processBooks(books, sections, queryParams) {
      // Assuming books is an array of books as received from the API
      this.sections = {}

      for (const section of Object.values(sections)) {
        const sectionId = section.id.toString()
        this.sections[sectionId] = {
          name: section.name,
          books: []
        }
      }

      for (const book of Object.values(books)) {
        const sectionId = book.section_id.toString()

        // Check if the book matches the filter criteria
        if (
          (!queryParams.section_id || sectionId === queryParams.section_id) &&
          (!queryParams.price || parseFloat(book.price) <= parseFloat(queryParams.price))
          // Add more filters as needed
        ) {
          if (this.sections[sectionId]) {
            this.sections[sectionId].books.push({
              id: book.id,
              name: book.name,
              author: book.author,
              price: book.price,
              image_url: book.image_url
            })
          }
        }
      }
    },
    issueBook(book) {
      // Implement issue book logic here
      ; (async () => {
        try {
          await this.$axios.post('/book/request', {
            book_id: book.id,
            user_id: localStorage.getItem('user_id'),
          });
          // Handle success
        } catch (error) {
          console.error('Error issuing book:', error)
        }
      })()
    },
  }
}
</script>

<style scoped>
.book-image {
  height: 200px;
  object-fit: cover;
}

.author-label {
  font-size: 1.2rem;
}

.price-label {
  font-size: 1.2rem;
}
</style>
