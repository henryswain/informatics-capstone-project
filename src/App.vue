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

    <!-- This is where your routed page will be displayed -->
    <router-view />
  </div>
</template>

<style scoped>
.navbar-brand {
  font-size: 1.5rem;
}
</style>
