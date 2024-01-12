<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            {{ isLoginForm ? 'Login' : 'Register' }}
          </div>
          <div class="card-body">
            <div class="mb-3 form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                id="toggleForm"
                v-model="isLoginForm"
              />
              <label class="form-check-label" for="toggleForm">
                {{ isLoginForm ? 'Switch to Register' : 'Switch to Login' }}
              </label>
            </div>
            <form @submit.prevent="isLoginForm ? login : register">
              <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input v-model="email" type="email" class="form-control" id="email" required>
              </div>
              <div v-if="!isLoginForm" class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input v-model="username" type="text" class="form-control" id="username" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input v-model="password" type="password" class="form-control" id="password" required>
              </div>
              <button type="submit" class="btn btn-primary" @click="login" v-if="isLoginForm">
  Login
</button>
<button type="submit" class="btn btn-primary" @click="register" v-else>
  Register
</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoginForm: true,
      email: '',
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await this.$axios.post('http://127.0.0.1:5000/login', {
          email: this.email,
          password: this.password
        });
        console.log('Login successful:', response.data);

        // Save user information to local storage
        this.saveUserInfo(response.data);

        // Redirect to the dashboard or another page
        this.redirectBasedOnRole(response.data.role);
      } catch (error) {
        console.error('Login failed:', error);
      }
    },
    async register() {
      try {
        const response = await this.$axios.post('http://127.0.0.1:5000/register', {
          email: this.email,
          username: this.username,
          password: this.password
        });
        alert(response.data.message)
        // Handle registration success, e.g., show a success message

        // Automatically switch to the login form after successful registration
        this.isLoginForm = true;
      } catch (error) {
        console.error('Registration failed:', error);
        alert(error.response.data.message)
      }
    },
    saveUserInfo(data) {
      // Save user information to local storage
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('email', data.email);
      localStorage.setItem('username', data.username);
      localStorage.setItem('role', data.role);
    },
    redirectBasedOnRole(role) {
      // Redirect based on user role
      if (role === 'librarian') {
        this.$router.push('/librarian');
      } else if (role === 'user') {
        this.$router.push('/user');
      }
    }
  }
};
</script>

<style scoped>
/* Add your custom styles here if needed */
</style>
