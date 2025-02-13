<script setup>
</script>

<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-primary navbar-dark">
      <div class="container-fluid">
        <router-link class="navbar-brand fw-bold" to="/">CareerQuest</router-link>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/find-jobs">Find Jobs</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/post-job">Post a Job</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/companies">Companies</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/career-advice">Career Advice</router-link>
            </li>
          </ul>

          <form class="d-flex me-3">
            <input class="form-control me-2" type="search" placeholder="Search jobs, companies..." />
            <button class="btn btn-outline-light" type="submit">Search</button>
          </form>

          <div class="d-flex align-items-center">
            <button class="btn btn-outline-light me-2">Login</button>
            <button class="btn btn-warning">Sign Up</button>

            <div class="dropdown ms-3">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
                <img src="@/assets/user.png" style="max-height: 30px;" alt="User" class="rounded-circle" />
              </button>
              <ul class="dropdown-menu dropdown-menu-end">
                <li>
                  <router-link class="dropdown-item" to="/profile">Profile</router-link>
                </li>
                <li>
                  <router-link class="dropdown-item" to="/saved-jobs">Saved Jobs</router-link>
                </li>
                <li>
                  <router-link class="dropdown-item" to="/settings">Settings</router-link>
                </li>
                <li>
                  <hr class="dropdown-divider" />
                </li>
                <li>
                  <router-link class="dropdown-item text-danger" to="/logout">Logout</router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <aside>
    <h2>Filter Your Search</h2>
    <div id="app">
        <label for="Job_Type">Job Type:</label>
        <select v-model="selectedJobType" id="Job_Type">
            <option value="all">All Job Types</option>
            <option value="Full-Time">Full-Time</option>
            <option value="Part-Time">Part-Time</option>
            <option value="Internship">Internship</option>
            <option value="Contract">Contract</option>
            <option value="Freelance">Freelance</option>
        </select>

        <label for="Industry">Industry:</label>
        <select v-model="selectedIndustry" id="Industry">
            <option value="all">All Industries</option>
            <option value="Technology">Technology</option>
            <option value="Healthcare">Healthcare</option>
            <option value="Finance">Finance</option>
            <option value="Education">Education</option>
            <option value="Marketing">Marketing</option>
            <option value="Engineering">Engineering</option>
            <option value="Retail">Retail</option>
            <option value="Hospitality">Hospitality</option>
            <option value="Government">Government</option>
            <option value="Manufacturing">Manufacturing</option>
        </select>

        <label for="Experience_Level">Experience Level:</label>
        <select v-model="selectedExperience" id="Experience_Level">
            <option value="all">All Levels</option>
            <option value="Entry-Level">Entry-Level</option>
            <option value="Mid-Level">Mid-Level</option>
            <option value="Senior-Level">Senior-Level</option>
            <option value="Executive">Executive</option>
        </select>

        <button @click.prevent="filterJobs">Find Jobs</button>
    </div>
    </aside>

    <!-- This is where your routed page will be displayed -->
    <router-view />
  </div>
</template>

<style scoped>
.navbar-brand {
  font-size: 1.5rem;
}
</style>
