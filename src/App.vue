<template>
  <div id="app">
    <!-- Desktop navbar -->
    <nav class="navbar navbar-expand bg-primary navbar-dark fixed-top d-none d-lg-flex">
      <div class="container-fluid">
        <router-link class="navbar-brand fw-bold" to="/home-page">CareerQuest</router-link>
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/find-jobs">Find Jobs</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/saved-jobs">Saved Jobs</router-link>
          </li>
        </ul>
        <form class="d-flex me-3" @submit.prevent="handleSubmit">
          <input
            class="form-control me-2"
            type="text"
            v-model="searchText"
            placeholder="Search jobs..."
          />
          <button class="btn btn-outline-light" type="text">Search</button>
        </form>
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
            <img
              src="@/assets/user.png"
              style="max-height: 30px;"
              alt="User"
              class="rounded-circle"
            />
          </button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><router-link class="dropdown-item" to="/profile">Profile</router-link></li>
            <li><router-link class="dropdown-item" to="/settings">Settings</router-link></li>
            <li><hr class="dropdown-divider" /></li>
            <!-- <li><router-link class="dropdown-item" to="/login">Login</router-link></li>
            <li><router-link class="dropdown-item" to="/register">Register</router-link></li>
            <li><router-link class="dropdown-item text-danger" to="/logout">Logout</router-link></li> -->
            <li>
              <div>
                <button v-if="!isAuthenticated" type="button" class="btn btn-link" data-bs-toggle="modal" data-bs-target="#authenticationModal">
                  Sign in/Sign up
                </button>
                <button v-else type="button" class="btn btn-link" data-bs-toggle="modal" data-bs-target="#authenticationModal">
                  Sign out
                </button>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Mobile navbar -->
    <nav class="navbar navbar-expand-lg bg-primary navbar-dark fixed-top d-lg-none">
      <div class="container-fluid">
        <router-link class="navbar-brand fw-bold" to="/">CareerQuest</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavMobile"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse flex-column align-items-center" id="navbarNavMobile">
          <ul class="navbar-nav mb-2 w-100 d-flex justify-content-center">
            <li class="nav-item">
              <router-link class="nav-link" :to="`/find-jobs?q=${searchText}`">Find Jobs</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/saved-jobs">Saved Jobs</router-link>
            </li>
          </ul>
          <form class="d-flex me-3" @submit.prevent="handleSubmit">
            <input
              class="form-control me-2"
              type="text"
              v-model="searchText"
              placeholder="Search jobs..."
            />
            <button class="btn btn-outline-light" type="text">Search</button>
          </form>
          <div class="dropdown w-100 d-flex justify-content-center">
            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
              <img
                src="@/assets/user.png"
                style="max-height: 30px;"
                alt="User"
                class="rounded-circle"
              />
            </button>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><router-link class="dropdown-item" to="/profile">Profile</router-link></li>
              <li><router-link class="dropdown-item" to="/settings">Settings</router-link></li>
              <li><hr class="dropdown-divider" /></li>
              <li>
                <div>
                  <button
                    v-if="!isAuthenticated"
                    type="button"
                    class="btn btn-link"
                    data-bs-toggle="modal"
                    data-bs-target="#authenticationModal"
                  >
                    Sign in/Sign up
                  </button>
                  <button
                    v-else
                    type="button"
                    class="btn btn-link"
                    data-bs-toggle="modal"
                    data-bs-target="#authenticationModal"
                  >
                    Sign out
                  </button>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>

    <!-- Authentication Modal -->
    <div class="modal fade" id="authenticationModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <h1>testing</h1>
          <authenticator>
            We can conditionally render content based on auth state if needed
          </authenticator>
        </div>
      </div>
    </div>
    <authenticator />

    <!-- Main Content -->
    <div style="margin-top: 70px;">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { Authenticator } from "@aws-amplify/ui-vue";
import "@aws-amplify/ui-vue/styles.css";
import { Amplify } from 'aws-amplify';
import outputs from '../amplify_outputs.json';
Amplify.configure(outputs);

import { Hub } from 'aws-amplify/utils';
import { getCurrentUser } from 'aws-amplify/auth';

const isAuthenticated = ref(false);

const closeModal = () => {

  console.log("close modal")
  // Select the element you want to fire the event on
  const modalElement = document.getElementById('authenticationModal');

  // Create the event, ensuring it matches the Bootstrap naming convention
  const event = new Event('dismiss.bs.modal', {
    bubbles: true, // Event will bubble up through the DOM tree
    cancelable: true // Event can be canceled
  });
  modalElement.dispatchEvent(event);
};

Hub.listen('auth', async ({ payload }) => {
  const { username, userId, signInDetails } = await getCurrentUser();
  switch (payload.event) {
    case 'signedIn':
      isAuthenticated.value = true;
      closeModal();
      break;
    case 'signedOut':
      isAuthenticated.value = false;
      closeModal();
      break;
    // ... other events
  }
});

const router = useRouter();
const searchText = ref("");

async function handleSubmit() {
  router.replace({ path: '/find-jobs', query: { q: searchText.value } });
  await nextTick();
}
</script>

<style scoped>
.navbar {
  z-index: 2000;
}
</style>

<style>
.modal {
  z-index: 2100 !important;
}
.modal-backdrop {
  z-index: 2050 !important;
}
.modal-dialog {
  margin-top: 80px;
}
</style>

<style>
.dark-mode .form-control,
.dark-mode input[type="text"],
.dark-mode input[type="email"],
.dark-mode input[type="search"],
.dark-mode input[type="password"],
.dark-mode select,
.dark-mode textarea,
.dark-mode .form-control {
  background-color: #444444 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .form-control::placeholder,
.dark-mode input[type="text"]::placeholder,
.dark-mode input[type="email"]::placeholder,
.dark-mode input[type="search"]::placeholder,
.dark-mode input[type="password"]::placeholder,
.dark-mode select::placeholder,
.dark-mode textarea::placeholder,
.dark-mode .form-control::placeholder {
  color: #cccccc !important;
}
.dark-mode .modal-content,
.dark-mode .modal-header,
.dark-mode .modal-body,
.dark-mode .modal-footer {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .btn-close {
  filter: invert(1);
}
</style>
