<template>
  <div class="container mt-5">
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
              <td>{{ formatRequestDate(request.request_date) }}</td>
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
      requests: []
    };
  },
  mounted() {
    this.getAllRequests();
  },
  methods: {
    async getAllRequests() {
      try {
        const response = await this.$axios.get('/book/request');
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
    },
    formatRequestDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    }
  }
};
</script>
