<template>
  <div class="login">
    <div class="container-fluid">
      <div class="row justify-content-center align-items-center min-vh-100">
        <!-- Background Image with Overlayed Login Form -->
        <div class="col-12 col-md-8 p-0">
          <div class="row g-0">
            <!-- Background Image Section -->
            <div class="col-lg-4 d-none d-lg-block login-bg-image"
              style="background-image: url('https://raw.githubusercontent.com/namansehwal/Assets/main/login.webp');">
            </div>

            <!-- Login Form Section -->
            <div class="col-12 col-lg-6">
              <div class="login__container border rounded p-4 shadow-lg animate__animated animate__zoomIn bg-white">
                <h1 class="text-center text-success mb-4">Login For the Larder Vault</h1>
                <form @submit.prevent="login">
                  <div class="mb-3">
                    <label for="username" class="form-label text-dark">Username:</label>
                    <input type="text" id="username" class="form-control text-dark" v-model="username"
                      placeholder="Type Here" />
                  </div>
                  <div class="mb-3">
                    <label for="password" class="form-label text-dark">Password:</label>
                    <input type="password" id="password" class="form-control text-dark" v-model="password"
                      placeholder="********" />
                  </div>
                  <button type="submit" class="login__signInButton btn btn-success w-100 mb-2">Login</button>
                  <button type="button" class="login__registerButton btn btn-outline-primary w-100"
                    @click="registerModal = true" data-bs-toggle="modal" data-bs-target="#signupModal">
                    Create your Account
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.login-bg-image {
  background-size: cover;
  background-position: center;
}

.login__container {
  font-family: 'Roboto', sans-serif;
  /* Changed to Roboto font */
  animation-duration: 1s;
  /* Adjust animation duration */
}

/* Add any additional styles for animations and fonts here */
</style>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const username = ref('')
const password = ref('')

const registerModal = ref(false)

const login = async () => {
  // ... (unchanged code for login function)
}
</script>
