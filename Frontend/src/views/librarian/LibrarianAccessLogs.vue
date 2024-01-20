<template>
  <div class="container mt-5">
    <!-- Display Access Logs and Filter -->
    <div class="card mt-4">
      <div class="card-header">Access Logs</div>
      <div class="card-body">
        <!-- Filter by Action -->
        <div class="mb-2">
          <label for="actionFilter" class="form-label">Filter by Action:</label>
          <select v-model="actionFilter" class="form-select" id="actionFilter">
            <option value="">All</option>
            <option value="Issued">Issued</option>
            <option value="Returned">Returned</option>
            <option value="Revoked">Revoked</option>
          </select>
        </div>

        <!-- Display Access Logs Table -->
        <table class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>User ID</th>
              <th>Book ID</th>
              <th>Status</th>
              <th>Issue Date</th>
              <th>Return Date</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="log in filteredLogs" :key="log.id">
              <td>{{ log.id }}</td>
              <td>{{ log.user_id }}</td>
              <td>{{ log.book_id }}</td>
              <td>{{ log.status }}</td>
              <td>{{ formatDateTime(log.issue_date) }}</td>
              <td v-if="log.return_date">{{ formatDateTime(log.return_date) }}</td>
              <td v-else>N/A</td>
              <td>
                <button v-if="log.status === 'Issued'" class="btn btn-danger btn-sm" @click="revokeAccesss(log.id)">Revoke</button>
                <button v-else class="btn btn-danger btn-sm" disabled>Revoke</button>
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
      logs: [],
      actionFilter: ''
    }
  },
  mounted() {
    this.getAllAccessLogs()
  },
  computed: {
    filteredLogs() {
      // Filter logs based on selected action
      return this.actionFilter
        ? this.logs.filter((log) => log.status === this.actionFilter)
        : this.logs
    }
  },
  methods: {
    async getAllAccessLogs() {
      try {
        const response = await this.$axios.get('/book/access')
        this.logs = response.data
      } catch (error) {
        console.error('Get Access Logs failed:', error)
      }
    },
    async revokeAccesss(id) {
      try {
        await this.$axios.put(`/book/access`, { id: id, revoke: 'True' })
        this.getAllAccessLogs()
      } catch (error) {
        console.error('Revoke Access failed:', error)
      }
    },
    formatDateTime(dateTimeString) {
      const options = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric'
      }
      return new Date(dateTimeString).toLocaleDateString('en-US', options)
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}

.card {
  margin-top: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.card-header {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}

.form-label {
  font-weight: bold;
}

.form-select {
  width: 200px;
}

.table {
  margin-top: 20px;
}
</style>
