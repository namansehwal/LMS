<template>
  <div>
    <!-- Top Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <!-- Logo and Name -->
        <router-link to="/librarian" class="navbar-brand" @click="toggleSidebar">
          <!-- Correct path to the image within the public folder -->
          <img src="/logo.png" alt="Logo" class="logo-img">
          LMS
        </router-link>

        <!-- Search Box -->
        <div class="search-box mx-auto">
          <input type="text" class="form-control" placeholder="Search...">
        </div>

        <!-- Logout Button -->
        <button @click="logout" class="btn btn-outline-danger ml-auto">Logout</button>

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
            <router-link to="/librarian/dashboard">Dashboard</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/sections">Sections</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/books">Books</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/accesslogs">Access Logs</router-link>
        </div>
        <div class="sidebar-header">
            <router-link to="/librarian/requests">Requests</router-link>
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
.logo-img {
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
  text-align: center;
  padding-bottom: 20px;
}

.main-content {
  transition: margin-left 0.3s;
  padding: 20px;
  margin-top: 60px;
}
</style>
