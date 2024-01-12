<template>
    <div>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
          <router-link to="/librarian/dashboard" class="navbar-brand">Librarian Dashboard</router-link>
          
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                <router-link to="/librarian/sections" class="nav-link">Manage Sections</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/librarian/books" class="nav-link">Manage Books</router-link>
              </li>
              <li class="nav-item">
                    <router-link to="/librarian/accesslogs" class="nav-link">Access Logs</router-link>
              </li>
            
              <li class="nav-item">
                    <router-link to="/librarian/requests" class="nav-link">Requests</router-link>
                </li>
              <li class="nav-item">
                <button @click="logout" class="btn btn-outline-danger">Logout</button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  
        <div class="container mt-5">
            <router-view></router-view>
        </div>    
    </div>
  </template>
  
  <script>

  export default {
    methods: {
      logout() {
        localStorage.clear();
        location.reload();
        
      }
    }
  };
  </script>
  
  