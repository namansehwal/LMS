<template>
  <div class="container mt-5">

    <!-- Add Request Form -->
    <div class="card mt-4">
      <div class="card-header bg-primary text-white">
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
      <div class="card-header bg-info text-white">
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
/* Center the card in the middle of the page */
.container {
  display: flex;
  justify-content: center;
  align-items: left;
  min-height: 50vh;
}

/* Add some spacing to the buttons for better readability */
.btn {
  margin-right: 5px;
}

/* Make the card header text bold */
.card-header {
  font-weight: bold;
}

/* Custom styles for the form headers */
.card-header.bg-primary,
.card-header.bg-info,
.card-header.bg-success {
  text-align: center;
  font-size: 1.2rem;
}

/* Add some spacing to the top of the table */
.table {
  margin-top: 15px;
}

/* Style table header */
.table thead th {
  background-color: #343a40;
  color: white;
}

/* Style alternating rows in the table */
.table-striped tbody tr:nth-child(odd) {
  background-color: #f8f9fa;
}

/* Hover effect for table rows */
.table-hover tbody tr:hover {
  background-color: #e2e6ea;
}
</style>