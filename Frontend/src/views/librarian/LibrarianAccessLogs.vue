<template>
    <div class="container mt-5">
      <h2>Access Logs</h2>
  
      <!-- Display Access Logs and Filter -->
      <div class="card mt-4">
        <div class="card-header">
          Access Logs
        </div>
        <div class="card-body">
          <!-- Filter by Action -->
          <div class="mb-3">
            <label for="actionFilter" class="form-label">Filter by Action:</label>
            <select v-model="actionFilter" class="form-select" id="actionFilter">
              <option value="">All</option>
              <option value="Issue">Issue</option>
              <option value="Return">Return</option>
            </select>
          </div>
  
          <!-- Display Access Logs Table -->
          <table class="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>User ID</th>
                <th>Book ID</th>
                <th>Action</th>
                <th>Log Date</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="log in filteredLogs" :key="log.id">
                <td>{{ log.id }}</td>
                <td>{{ log.user_id }}</td>
                <td>{{ log.book_id }}</td>
                <td>{{ log.action }}</td>
                <td>{{ log.log_date }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        logs: [],
        actionFilter: ''
      };
    },
    mounted() {
      this.getAllAccessLogs();
    },
    computed: {
      filteredLogs() {
        // Filter logs based on selected action
        return this.actionFilter
          ? this.logs.filter(log => log.action === this.actionFilter)
          : this.logs;
      }
    },
    methods: {
      async getAllAccessLogs() {
        try {
          const response = await this.$axios.get('/access-log');
          this.logs = response.data;
        } catch (error) {
          console.error('Get Access Logs failed:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  