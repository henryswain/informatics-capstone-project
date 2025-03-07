<template>
    <div class="register-page">
      <h2>Signup Form</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required />
        </div>
  
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required />
        </div>
  
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required />
          <div class="password-hint">
            Password must be at least 8 characters long, and include at least one uppercase letter, one lowercase letter, one number, and one special character.
          </div>
          <div class="password-strength">
            <div :class="passwordStrength"></div>
          </div>
        </div>
  
        <div class="form-group">
          <label for="confirmPassword">Confirm Password</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required />
        </div>
  
        <button type="submit">Signup</button>
      </form>
  
      <p id="message">{{ message }}</p>
    </div>
  </template>
  
  <style scoped>
  .container {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
  }
  
  h2 {
    margin-bottom: 20px;
    text-align: center;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    border: none;
    color: white;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #4cae4c;
  }
  
  .password-hint {
    font-size: 0.9em;
    color: #666;
    margin-top: 5px;
  }
  
  .password-strength {
    margin-top: 5px;
  }
  
  .password-strength div {
    height: 5px;
    border-radius: 4px;
  }
  
  .weak {
    width: 33%;
    background-color: red;
  }
  
  .medium {
    width: 66%;
    background-color: orange;
  }
  
  .strong {
    width: 100%;
    background-color: green;
  }
  </style>
  