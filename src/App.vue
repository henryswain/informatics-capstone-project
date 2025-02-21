<template>
  <div id="app">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg bg-primary navbar-dark fixed-top">
      <div class="container-fluid">
        <router-link class="navbar-brand fw-bold" to="/">CareerQuest</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/find-jobs">Find Jobs</router-link>
            </li>
          </ul>
          <form class="d-flex me-3">
            <input class="form-control me-2" type="search" placeholder="Search jobs, companies..." />
            <button class="btn btn-outline-light" type="submit">Search</button>
          </form>
          <div class="d-flex align-items-center">
            <div class="dropdown ms-3">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
                <img src="@/assets/user.png" style="max-height: 30px;" alt="User" class="rounded-circle" />
              </button>
              <ul class="dropdown-menu dropdown-menu-end">
                <li><router-link class="dropdown-item" to="/profile">Profile</router-link></li>
                <li><router-link class="dropdown-item" to="/saved-jobs">Saved Jobs</router-link></li>
                <li><router-link class="dropdown-item" to="/settings">Settings</router-link></li>
                <li><hr class="dropdown-divider" /></li>
                <li><router-link class="dropdown-item text-danger" to="/logout">Logout</router-link></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <!-- Only show the filter sidebar on the Find Jobs page -->
        <div v-if="$route.path === '/find-jobs'" class="filter-sidebar">
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

        <!-- Main Content Area for Routed Pages -->
        <div :class="{'main-content': $route.path === '/find-jobs', 'main-content-full': $route.path !== '/find-jobs'}">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

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
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 2000;
}

.filter-sidebar {
  position: fixed;
  top: 70px;
  left: 0;
  width: 250px;
  height: calc(100% - 70px);
  overflow-y: auto;
  padding: 1rem;
  background-color: #f5f7fa;
  border-right: 1px solid #ddd;
  z-index: 1000;
}

.main-content {
  margin-top: 70px;
  margin-left: 260px;
  padding: 2rem;
}

.main-content-full {
  margin-top: 70px;
  margin-left: 0;
  padding: 2rem;
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
</style>