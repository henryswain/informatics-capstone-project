<template>
  <div id="app">
    <!--Desktop navbar-->
    <nav class="navbar navbar-expand bg-primary navbar-dark fixed-top d-none d-lg-flex">
      <div class="container-fluid">
        <!-- Brand on the far left -->
        <router-link class="navbar-brand fw-bold" to="/home-page">CareerQuest</router-link>

        <!-- nav links -->
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/find-jobs">Find Jobs</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/saved-jobs">Saved Jobs</router-link>
          </li>
        </ul>

        <!-- search -->
        <form class="d-flex me-3" @submit.prevent="handleSubmit">
          <input
            class="form-control me-2"
            type="text"
            v-model="searchText"
            placeholder="Search jobs..."
          />
          <button class="btn btn-outline-light" type="text">Search</button>
        </form>

        <!-- profile/saved jobs dropdown -->
        <div class="dropdown">
          <button
            class="btn btn-secondary dropdown-toggle"
            type="button"
            data-bs-toggle="dropdown"
          >
            <img
              src="@/assets/user.png"
              style="max-height: 30px;"
              alt="User"
              class="rounded-circle"
            />
          </button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><router-link class="dropdown-item" to="/profile">Profile</router-link></li>
            <li><router-link class="dropdown-item" to="/Settings">Settings</router-link></li>
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

    <!--smaller screen/mobile navbar -->
    <nav class="navbar navbar-expand-lg bg-primary navbar-dark fixed-top d-lg-none">
      <div class="container-fluid">
        <!-- Brand -->
        <router-link class="navbar-brand fw-bold" to="/">CareerQuest</router-link>

        <!-- mobile menu toggle -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavMobile"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div
          class="collapse navbar-collapse flex-column align-items-center"
          id="navbarNavMobile"
        >
          <!-- centering mobile nav view -->
          <ul class="navbar-nav mb-2 w-100 d-flex justify-content-center">
            <li class="nav-item">
              <router-link class="nav-link" :to="`/find-jobs?q=${searchText}`">Find Jobs</router-link>
            </li>
             <li class="nav-item">
            <router-link class="nav-link" to="/saved-jobs">Saved Jobs</router-link>
          </li>
          </ul>

          <!-- centers search bar -->
          <form class="d-flex me-3" @submit.prevent="handleSubmit">
            <input
              class="form-control me-2"
              type="text"
              v-model="searchText"
              placeholder="Search jobs..."
            />
            <button class="btn btn-outline-light" type="textt">Search</button>
          </form>

          <!-- centers profile dropdown -->
          <div class="dropdown w-100 d-flex justify-content-center">
            <button
              class="btn btn-secondary dropdown-toggle"
              type="button"
              data-bs-toggle="dropdown"
            >
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
      </div>
    </nav>


      <!-- authentication modal -->
  <div class="modal fade" id="authenticationModal" tabindex="-1" aria-labelledby="authenticationModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <!-- Basic authenticator without slots -->
          <authenticator>
            <template v-slot="{ user, signOut }">
              <h1>Hello {{ user.username }}!</h1>
              <button class="btn btn-primary" @click="signOut">Sign Out</button>
            </template>
          </authenticator>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" aria-label="Close">Close</button>
        </div>
      </div>
    </div>
  </div>


  <!-- main content  -->
    <div style="margin-top: 70px;">
      <!-- Only use grid layout on the Find Jobs page -->
      <div v-if='$route.path === "/find-jobs"' class="grid-container">
        <!-- Filter Section -->
        <div class="filter-section">
          <div class="card filter-card mb-4">
            <div class="card-body">
              <h5 class="card-title">Filter Your Search</h5>
              <div class="filter-group">
                <h6>Job Type</h6>
                <div class="filter-options">
                  <button
                    v-for="option in jobTypeOptions"
                    :key="option"
                    :class="['filter-box', { active: filters.jobTypes.includes(option) }]"
                    @click="toggleFilter('jobTypes', option)"
                  >
                    {{ option }}
                  </button>
                </div>
              </div>
              <div class="filter-group mt-3">
                <h6>Industry</h6>
                <div class="filter-options">
                  <button
                    v-for="option in industryOptions"
                    :key="option"
                    :class="['filter-box', { active: filters.industries.includes(option) }]"
                    @click="toggleFilter('industries', option)"
                  >
                    {{ option }}
                  </button>
                </div>
              </div>
              <div class="filter-group mt-3">
                <h6>Location</h6>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter city or zip"
                  v-model="filters.location"
                />
              </div>
              <button class="btn btn-primary w-100 mt-3" @click="applyFilters">
                Apply Filters
              </button>
            </div>
          </div>
        </div>
        <!-- Jobs Section -->
        <div class="jobs-section">
          <router-view />
        </div>
      </div>
      <!-- full width for other content other than find-jobs -->
      <div v-else class="main-content-full">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { nextTick } from 'vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

  import { Amplify } from 'aws-amplify';
  import outputs from '../amplify_outputs.json';

  Amplify.configure(outputs);

  import { Authenticator } from "@aws-amplify/ui-vue";
  import "@aws-amplify/ui-vue/styles.css";

  import { Hub } from 'aws-amplify/utils';
const isAuthenticated = ref(false);

// Close the modal programmatically
const closeModal = () => {

  console.log("close modal")
  // Select the element you want to fire the event on
  const modalElement = document.getElementById('authenticationModal');

  // Create the event, ensuring it matches the Bootstrap naming convention
  const event = new Event('dismiss.bs.modal', {
    bubbles: true, // Event will bubble up through the DOM tree
    cancelable: true // Event can be canceled
  });

  // Dispatch the event
  modalElement.dispatchEvent(event);
};
import { getCurrentUser } from 'aws-amplify/auth';


console.log("isAutheniccated.value", isAuthenticated.value)
Hub.listen('auth', async({ payload }) => {
  const { username, userId, signInDetails } = await getCurrentUser();

  switch (payload.event) {
    case 'signedIn':
      isAuthenticated.value = true;
      closeModal()
      console.log('user have been signedIn successfully.');
      console.log("username", username);
      console.log("user id", userId);
      console.log("sign-in details", signInDetails);
      break;
    case 'signedOut':
      isAuthenticated.value = false;
      closeModal()

      console.log('user have been signedOut successfully.');
      console.log("username", username);
      console.log("user id", userId);
      console.log("sign-in details", signInDetails);
      break;
    case 'tokenRefresh':
      console.log('auth tokens have been refreshed.');
      break;
    case 'tokenRefresh_failure':
      console.log('failure while refreshing auth tokens.');
      break;
    case 'signInWithRedirect':
      console.log('signInWithRedirect API has successfully been resolved.');
      break;
    case 'signInWithRedirect_failure':
      console.log('failure while trying to resolve signInWithRedirect API.');
      break;
    case 'customOAuthState':
      logger.info('custom state returned from CognitoHosted UI');
      break;
  }
});
  
const router = useRouter();

const searchText = ref("");

const handleSubmit = async () => {
  router.replace({ path: '/find-jobs', query: { q: searchText.value } });
  console.log("handleInputChange called");
  console.log("searchText: ", searchText.value);
  await nextTick();
};

const jobTypeOptions = ['Full-Time', 'Part-Time', 'Internship', 'Contract', 'Freelance'];
const industryOptions = ['Technology', 'Healthcare', 'Finance', 'Education', 'Marketing'];

const filters = ref({
  jobTypes: [],
  industries: [],
  location: '',
});

function toggleFilter(filterCategory, option) {
  const index = filters.value[filterCategory].indexOf(option);
  if (index === -1) {
    filters.value[filterCategory].push(option);
  } else {
    filters.value[filterCategory].splice(index, 1);
  }
}

function applyFilters() {
  console.log('Applied filters:', filters.value);
}
</script>

<style scoped>
.navbar {
  z-index: 2000;
}
.grid-container {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 20px;
  padding: 1rem;
}

/* left hand filter section */
.filter-section {
  padding: 1rem;
  background-color: #f5f7fa;
  border-right: 1px solid #ddd;
}

/* right hand jobs section */
.jobs-section {
  padding: 1rem;
}

.main-content-full {
  padding: 1rem;
}

.filter-card {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.filter-group h6 {
  margin-bottom: 0.5rem;
  color: #343a40;
}

.filter-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.filter-box {
  border: 1px solid #ccc;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  background-color: #fff;
  cursor: pointer;
  transition: background-color 0.2s, border-color 0.2s;
}

.filter-box:hover {
  background-color: #e9ecef;
}

.filter-box.active {
  background-color: #007bff;
  color: #fff;
  border-color: #007bff;
}

/* responsiveness stacking grid columns */
@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: 1fr;
  }
}
</style>

<!-- Modal styles -->
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

<!-- Global Dark Mode Overrides -->
<style>

/* 1. Inputs, including password fields, in dark mode */
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

/* Placeholder text */
.dark-mode input[type="text"]::placeholder,
.dark-mode input[type="email"]::placeholder,
.dark-mode input[type="search"]::placeholder,
.dark-mode input[type="password"]::placeholder,
.dark-mode select::placeholder,
.dark-mode textarea::placeholder,
.dark-mode .form-control::placeholder {
  color: #cccccc !important;
}

/* 2. Profile Page */
.dark-mode .profile-container,
.dark-mode .profile-header,
.dark-mode .profile-details,
.dark-mode .profile-picture-container,
.dark-mode .profile-actions {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}

/* Force all children to inherit dark mode colors */
.dark-mode .profile-container *,
.dark-mode .profile-header *,
.dark-mode .profile-details *,
.dark-mode .profile-picture-container *,
.dark-mode .profile-actions * {
  color: #ffffff !important;
}


.dark-mode .profile-picture {
  background-color: #444444 !important;
  border-color: #555555 !important;
}

.dark-mode .btn-upload,
.dark-mode .btn-success,
.dark-mode .btn-primary,
.dark-mode .btn-secondary {
  background-color: #444444 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}


.dark-mode .signup-container,
.dark-mode .signup-container * {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}

/* 4. Saved Jobs Page */
.dark-mode .saved-jobs-container,
.dark-mode .saved-jobs-container * {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}


.dark-mode .saved-jobs-container .job-item {
  background-color: #444444 !important;
  border-color: #555555 !important;
}

/* Buttons on Saved Jobs page */
.dark-mode .saved-jobs-container .btn.btn-primary {
  background-color: #007bff !important;
  color: #ffffff !important;
  border-color: #007bff !important;
}
.dark-mode .saved-jobs-container .btn.btn-danger {
  background-color: #b02a37 !important;
  color: #ffffff !important;
  border-color: #b02a37 !important;
}

/* 5. Modal Content (e.g., job descriptions, profile modals, etc.) */
.dark-mode .modal-content,
.dark-mode .modal-header,
.dark-mode .modal-body,
.dark-mode .modal-footer {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}

.dark-mode .filter-section,
.dark-mode .filter-section * {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .btn-close {
  filter: invert(1);
}

</style>

