<template>
    <div>
      <h2>User Profile</h2>
      <form @submit.prevent="updateProfile">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" v-model="username" class="form-control" id="username" required>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" v-model="email" class="form-control" id="email" required>
        </div>
        <button type="submit" class="btn btn-primary">Update Profile</button>
      </form>
  
      <button @click="deleteProfile" class="btn btn-danger mt-3">Delete Profile</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: "",
        email: "",
        userId: localStorage.getItem('user_id')
      };
    },
    mounted() {
      // Fetch user data when the component is mounted
      this.fetchUserProfile();
    },
    methods: {
      fetchUserProfile() {
        this.$axios.get(`/profile/${this.userId}`)
            .then(response => {
                const userData = response.data;
                this.username = userData.username;
                this.email = userData.email;
            })
            .catch(error => {
                console.error("Error fetching user profile:", error);
            });
      },
      updateProfile() {
        const data = {
          id: this.userId,
          username: this.username,
          email: this.email,
        };
  
        this.$axios.put(`/profile/${this.userId}`, data)
          .then(response => {
            alert(response.data.message);
          })
          .catch(error => {
            console.error("Error updating user profile:", error);
          });
      },
      deleteProfile() {
        // Send a DELETE request to delete the user profile
        const data = {
          id: this.userId,
        };
  
        if (window.confirm("Are you sure you want to delete your profile?")) {
          this.$axios.delete(`/profile/${this.userId}`, { data })
            .then(response => {
              console.log(response.data.message);

              // Optionally, redirect the user to a login page or another route
              alert(response.data.message);
              this.$router.push('/login');
              localStorage.clear();

            })
            .catch(error => {
              console.error("Error deleting user profile:", error);
            });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add any custom styles here */
  </style>
  