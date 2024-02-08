User
<template>
  <div>
    <!-- Top Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <!-- Logo and Name -->
        <router-link to="/user" class="navbar-brand" @click="toggleSidebar">
          <!-- Correct path to the image within the public folder -->
          <h1>🏛️ Library 🏛️ </h1>
        </router-link>

        <!-- Search Box -->
        <div class="search-box d-flex">
          <input type="text" class="form-control" placeholder="Search..." v-model="searchQuery" @input="updateSearchQuery">
          <h1 class="m-1"><a class="pe-auto text-decoration-none" @click="searchBooks">🧐</a></h1>
        </div>

        <!-- Logout Button -->
        <button @click="logout" class="btn btn-danger ml-auto">Logout</button>

        <!-- Mobile Menu Button -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
    </nav>

    <!-- Sidebar Menu -->
    <div v-if="sidebarVisible" class="sidebar">
      <div class="sidebar-header">
        <router-link to="/user/books" class="text-decoration-none text-muted"><h2>📖 Books</h2></router-link>
      </div>
      <div class="sidebar-header">
        <router-link to="/user/profile" class="text-decoration-none text-muted"><h2>👤 Profile</h2></router-link>
      </div>
      <div class="sidebar-header">
        <router-link to="/user/space" class="text-decoration-none text-muted"><h2>🚀 My Space</h2></router-link>
      </div>
      <div class="sidebar-header">
        <router-link to="/user/read" class="text-decoration-none text-muted"><h2>😴 Read</h2></router-link>
      </div>  
    </div>

    <!-- Main Content -->
    <div class="main-content " :style="{ marginLeft: sidebarVisible ? '250px' : '0' }">
      <router-view></router-view>
      <div  class="text-muted" v-if="$route.path === '/user'">
      <h1 class="m-2">Welcome to the Library</h1>
      <hr>
      <p class="h2">You can search for books, view your profile, and manage your space from the sidebar.</p>
      <br><br><br><br><br>
      <h3 class="m-1 h1">📚 Policy:</h3>
      <p class="m-5 h2"> ⚝ You can borrow a maximum of 5 books at a time.</p>
      <p class="m-5 h2">⚝ You can keep the books for a maximum of 7 days.</p> 
    </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const searchQuery = ref('');

    const searchBooks =  async () => {
      console.log('Search books method called');
      try {
        await store.dispatch('searchBooks', searchQuery.value);
        searchQuery.value = '';
      } catch (error) {
        console.error('Error searching books:', error);
      }
    };

    const updateSearchQuery = () => {
      store.commit('setSearchQuery', searchQuery.value);
    };

    return {
      searchQuery,
      searchBooks,
      updateSearchQuery,
    };
  },
  data() {
    return {
      sidebarVisible: false,
    };
  },
  methods: {
    toggleSidebar() {
      this.sidebarVisible = !this.sidebarVisible;
    },
    logout() {
      localStorage.clear();
      location.reload();
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
.img {
  max-width: 40px;
  margin-right: 10px;
}

.search-box {
  width: 300px;
}

.sidebar {
  width: 250px;
  background-color: #9eabb4;
  position: fixed;
  height: 100%;
  overflow-y: auto;
  padding-top: 30px;
  margin-top: 0;
  z-index: 1000;
}

.sidebar-visible {
  display: block;
}

.sidebar-header {
  text-align: left;
  padding-bottom: 20px;
  margin-left: 20px;
}

.main-content {
  transition: margin-left 0.3s;
  padding: 20px;
  margin-top: 60px;
}
</style>