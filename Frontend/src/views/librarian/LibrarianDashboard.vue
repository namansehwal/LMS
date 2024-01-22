<template>
  <div>
    <!-- Top Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <!-- Logo and Name -->
        <router-link to="/librarian" class="navbar-brand" @click="toggleSidebar">
          <!-- Correct path to the image within the public folder -->
          <img src="/admin.jpg" alt="admin" class="img">
          LMS (Librarian)
        </router-link>

        <!-- Search Box -->
        <div class="search-box mx-auto">
          <input type="text" class="form-control" placeholder="Search...">
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
            <router-link to="/librarian/sections"><img src="/sections.jpg" alt="sections" class="img">Sections</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/books"><img src="/lms_books.jpg" alt="lms_books" class="img">Books</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/accesslogs"><img src="/access.png" alt="access" class="img">Access Logs</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/requests"><img src="/request.jpeg" alt="request" class="img">Requests</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/stats_and_graphs"><img src="/dashboard.jpg" alt="dashboard" class="img">Stats_and_Graphs</router-link>    
        </div>
    </div>

    <!-- Main Content -->
    <div class="main-content" :style="{ marginLeft: sidebarVisible ? '250px' : '0' }">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
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
        }
    }
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
