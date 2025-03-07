<template>
    <div class="Login-page">
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="email">Email Address</label>
          <input 
            type="email" 
            class="form-control" 
            id="email" 
            v-model="email" 
            aria-describedby="emailHelp" 
            placeholder="Enter email" 
            required
          />
          <small id="emailHelp" class="form-text text-muted">
            We'll never share your email with anyone else.
          </small>
        </div>
  
        <div class="form-group">
          <label for="password">Password</label>
          <input 
            type="password" 
            class="form-control" 
            id="password" 
            v-model="password" 
            placeholder="Password" 
            required
          />
        </div>
  
        <div class="form-check">
          <input 
            type="checkbox" 
            class="form-check-input" 
            id="rememberMe" 
            v-model="rememberMe"
          />
          <label class="form-check-label" for="rememberMe">
            Remember me
          </label>
        </div>
  
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: "",
        password: "",
        rememberMe: false,
      };
    },
    methods: {
      submitForm() {
        console.log("Email:", this.email);
        console.log("Password:", this.password);
        console.log("Remember Me:", this.rememberMe);
      }
    }
  };
  </script>
  
  <style scoped>
  .login-page {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  </style>
  