<template>
    <div>
  
      <!-- Book Requests Table -->
      <div v-if="filteredBookRequests.length > 0">
        <h3>Book Requests</h3>
        <table class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Book Name</th>
              <th>Request Date</th>
              <th>Status</th>
              <th>Action</th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="request in filteredBookRequests" :key="request.id">
              <td>{{ request.id }}</td>
              <td>{{ request.book_name }}</td>
              <td>{{ request.request_date }}</td>
              <td>{{ request.status }}</td>
              <td>
                <button class="btn btn-danger" v-if="request.status === 'Pending'" @click="deleteRequest(request.id)">Cancel</button>
                <button class="btn btn-danger" v-if="request.status === 'Rejected'" @click="deleteRequest(request.id)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else>
        <hr>
        <h1>No book requests available.</h1>
      </div>
  
      <!-- Issued Books Table -->
      <div v-if="filteredIssuedBooks.length > 0">
        <h3>Issued Books</h3>
        <table class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Book Name</th>
              <th>Status</th>
              <th>Issue Date</th>
              <th>Return Date</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="accessLog in filteredIssuedBooks" :key="accessLog.id">
              <td>{{ accessLog.id }}</td>
              <td>{{ accessLog.book_name }}</td>
              <td>{{ accessLog.status }}</td>
              <td>{{ accessLog.issue_date }}</td>
              <td>{{ accessLog.return_date }}</td>
              <td>
                <button class="btn btn-danger" v-if="accessLog.status === 'Issued'" @click="returnBook(accessLog.id)">Return</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else>
        <hr>
        <h1>No issued books available.</h1>
      </div>
    </div>
  </template>
  
  
  
  <script>
  export default {
    data() {
      return {
        bookRequests: [],
        issuedBooks: [],
      };
    },
    computed: {
      filteredBookRequests() {
        const user_id = localStorage.getItem('user_id');
        return this.bookRequests.filter(request => request.user_id === parseInt(user_id));
      },
      filteredIssuedBooks() {
        const user_id = localStorage.getItem('user_id');
        return this.issuedBooks.filter(accessLog => accessLog.user_id === parseInt(user_id));
      },
    },
    mounted() {
      this.fetchBookRequests();
      this.fetchIssuedBooks();
    },
    methods: {
      fetchBookRequests() {
        this.$axios.get('/book/request')
          .then(response => {
            this.bookRequests = response.data;
          })
          .catch(error => {
            console.error('Error fetching book requests', error);
          });
      },
      fetchIssuedBooks() {
        this.$axios.get('/book/access')
          .then(response => {
            this.issuedBooks = response.data;
          })
          .catch(error => {
            console.error('Error fetching issued books', error);
          });
      },

      deleteRequest(requestId) {
  this.$axios({
    method: 'delete',
    url: `/book/request`,
    headers: {
      'Content-Type': 'application/json',
    },
    data: {
      id: requestId,
    },
  })
  .then(response => {
    alert(response.data.message);
    this.fetchBookRequests();
  })
  .catch(error => {
    console.error('Error deleting request', error);
  });
},

returnBook(accessLogId) {
  this.$axios({
    method: 'put',
    url: `/book/access`,
    headers: {
      'Content-Type': 'application/json',
    },
    data: {
      id: accessLogId,
      returned: "True",
    },
  })
  .then(() => {
    // Refresh the issued books
    alert('Book returned successfully');
    this.fetchIssuedBooks();
  })
  .catch(error => {
    console.error('Error returning book', error);
  });
},

    },
  };
  </script>
  
  
  
  <style scoped>
  /* Add Bootstrap 4 styles here */
  
  .table {
    width: 100%;
    margin-bottom: 1rem;
    color: #212529;
    border-collapse: collapse;
  }
  
  .table th,
  .table td {
    padding: 0.75rem;
    vertical-align: top;
    border-top: 1px solid #dee2e6;
  }
  
  .table thead th {
    vertical-align: bottom;
    border-bottom: 2px solid #dee2e6;
  }
  
  .table tbody + tbody {
    border-top: 2px solid #dee2e6;
  }
  
  .table .table {
    background-color: #fff;
  }
  
  .table-sm th,
  .table-sm td {
    padding: 0.3rem;
  }
  
  .table-bordered {
    border: 1px solid #dee2e6;
  }
  
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #dee2e6;
  }
  
  .table-bordered thead th,
  .table-bordered thead td {
    border-bottom-width: 2px;
  }
  
  .table-borderless th,
  .table-borderless td,
  .table-borderless thead th,
  .table-borderless tbody + tbody {
    border: 0;
  }
  
  .table-striped tbody tr:nth-of-type(odd) {
    background-color: rgba(0, 0, 0, 0.05);
  }
  
  .table-hover tbody tr:hover {
    background-color: rgba(0, 0, 0, 0.075);
  }
  
  </style>
  