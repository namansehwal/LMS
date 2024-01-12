<template>
    <div class="container mt-5">
      <h2>Book Requests</h2>
  
      <!-- Add Request Form -->
      <div class="card mt-4">
        <div class="card-header">
          Add Request
        </div>
        <div class="card-body">
          <form @submit.prevent="addRequest">
            <div class="mb-3">
              <label for="userId" class="form-label">User ID</label>
              <input v-model="newRequest.user_id" type="number" class="form-control" id="userId" required>
            </div>
            <div class="mb-3">
              <label for="bookId" class="form-label">Book ID</label>
              <input v-model="newRequest.book_id" type="number" class="form-control" id="bookId" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Request</button>
          </form>
        </div>
      </div>
  
      <!-- Display Requests -->
      <div class="card mt-4">
        <div class="card-header">
          All Requests
        </div>
        <div class="card-body">
          <table class="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>User ID</th>
                <th>Book ID</th>
                <th>Request Date</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="request in requests" :key="request.id">
                <td>{{ request.id }}</td>
                <td>{{ request.user_id }}</td>
                <td>{{ request.book_id }}</td>
                <td>{{ request.request_date }}</td>
                <td>{{ request.status }}</td>
                <td>
                  <button @click="cancelRequest(request.id)" class="btn btn-danger btn-sm">Cancel</button>
                </td>
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
        newRequest: {
          user_id: '',
          book_id: ''
        },
        requests: []
      };
    },
    mounted() {
      this.getAllRequests();
    },
    methods: {
      async addRequest() {
        try {
          const response = await this.$axios.post('/request', this.newRequest);
          this.getAllRequests();
          // Clear the form after adding the request
          this.newRequest = {
            user_id: '',
            book_id: ''
          };
        } catch (error) {
          console.error('Add Request failed:', error);
        }
      },
      async getAllRequests() {
        try {
          const response = await this.$axios.get('/request');
          this.requests = response.data;
        } catch (error) {
          console.error('Get Requests failed:', error);
        }
      },
      async cancelRequest(requestId) {
        try {
          await this.$axios.delete(`/request/${requestId}`);
          this.getAllRequests();
        } catch (error) {
          console.error('Cancel Request failed:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  