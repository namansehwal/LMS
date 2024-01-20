<template>
  <div>
    <!-- Top Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" style="z-index: 1100;">
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
    <div class="main-content" style="padding-top: 30px; margin-top: 50px;">
    <div id="wrapper">
    <div class="d-flex flex-column" id="content-wrapper">
      <div id="content">
        <div class="container-fluid">
          <div class="d-sm-flex justify-content-between align-items-center mb-4"></div>
          <div class="row">
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-start-primary py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col me-2">
                      <div class="text-uppercase text-primary fw-bold text-xs mb-1">
                        <span class="fs-5">Total Issued</span>
                      </div>
                      <div class="text-dark fw-bold h5 mb-0">
                        <span>₹ {{ res.total_issued_books }}</span>
                      </div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-calendar fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-start-success py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col me-2">
                      <div class="text-uppercase text-success fw-bold text-xs mb-1">
                        <span class="fs-5">Penalty on Overdues</span>
                      </div>
                      <div class="text-dark fw-bold h5 mb-0">
                        <span>₹ {{ res.total_penalty }}</span>
                      </div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-start-info py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col me-2">
                      <div class="text-uppercase text-info fw-bold text-xs mb-1">
                        <span class="fs-5">Books</span>
                      </div>
                      <div class="row g-0 align-items-center">
                        <div class="col-auto">
                          <div class="text-dark fw-bold h5 mb-0 me-3">
                            <span>{{ res.total_books }} ({{ res.unavailable }} Unavailable)</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-start-warning py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col me-2">
                      <div class="text-uppercase text-warning fw-bold text-xs mb-1">
                        <span class="fs-5">User's Count</span>
                      </div>
                      <div class="text-dark fw-bold h5 mb-0">
                        <span>{{ res.total_users }}</span>
                      </div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-comments fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-7 col-xl-8">
              <div class="card shadow mb-4">
                <div class="card-header d-flex justify-content-between align-items-center">
                  <h6 class="text-primary fw-bold m-1">Top 5 most issued books</h6>
                </div>
                <div class="card-body m-2">
                  <div class="chart-area" style="width: 1100px; height: 550px">
                    <canvas id="barchart"></canvas>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-5 col-xl-4">
              <div class="card shadow mb-4">
                <div class="card-header d-flex justify-content-between align-items-center">
                  <h6 class="text-primary fw-bold m-1">Number of books in each section</h6>
                </div>
                <div class="card-body">
                  <div class="chart-area" style="width: 100%; height: 100%">
                    <canvas id="polar-chart"></canvas>
                  </div>
                </div>
              </div>
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
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      sidebarVisible: false,
      materials: [],
      res: {} // Initialize an empty object to store the dictionary
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    toggleSidebar() {
      this.sidebarVisible = !this.sidebarVisible;
    },
    logout() {
      localStorage.clear();
      location.reload();
    },
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:5000/summary')
        console.log('Response:', response.data);
        this.materials = Object.entries(response.data).map(([name, value]) => ({ name, value }))
        
        // Convert materials to a dictionary
        this.res = this.materials.reduce((obj, material) => {
          obj[material.name] = material.value
          return obj
        }, {})
        this.renderBarChart()
        this.renderPolarChart()
      } catch (error) {
        console.error(error)
      }
    },
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // swap elements
      }
      return array;
    },
    renderPolarChart() {
      const ctx = document.getElementById('polar-chart').getContext('2d');
      const sections = this.res.section_wise_book_count;

      new Chart(ctx, {
        type: 'polarArea',
        data: {
          labels: this.shuffleArray(Object.keys(sections)),
          datasets: [{
            data: this.shuffleArray(Object.values(sections)),

            backgroundColor: this.shuffleArray([
              'rgba(255, 99, 132, 0.5)',
              'rgba(255, 159, 64, 0.5)',
              'rgba(255, 205, 86, 0.5)',
              'rgba(75, 192, 192, 0.5)',
              'rgba(54, 162, 235, 0.5)',
              'rgba(153, 102, 255, 0.5)',
              'rgba(201, 203, 207, 0.5)'
            ]),
            borderWidth: 1
          }]
        },

      });
    },
    renderBarChart() {
      const ctx = document.getElementById('barchart').getContext('2d');
      const books = this.res.top_books;

      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: books.map(book => book.book_name),
          datasets: [{
            label: 'Issued',
            data: books.map(book => book.average_rating),
            backgroundColor: this.shuffleArray([
              'rgba(255, 99, 132, 0.5)',
              'rgba(54, 162, 235, 0.5)',
              'rgba(255, 206, 86, 0.5)',
              'rgba(75, 192, 192, 0.5)',
              'rgba(153, 102, 255, 0.5)',
              'rgba(255, 159, 64, 0.5)',
              'rgba(199, 199, 199, 0.5)',
              'rgba(83, 102, 255, 0.5)',
              'rgba(40, 159, 64, 0.5)',
              'rgba(255, 99, 132, 0.5)'
            ]),

            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
      // ctx.canvas.width = container.clientWidth;
      // ctx.canvas.height = container.clientHeight;
    }
  }
}      
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

@media (max-width: 768px) {
    .sidebar {
      width: 100%;
    }
    .main-content {
      margin-left: 0;
    }
  }
</style>
