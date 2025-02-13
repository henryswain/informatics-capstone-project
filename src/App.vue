<script setup>
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-primary navbar-dark">
    <div class="container-fluid">
      <!-- Logo -->
      <a class="navbar-brand fw-bold" href="#">TalentHub</a>

      <!-- Mobile Toggle Button -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <!-- Left Side Links -->
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" href="#">Find Jobs</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Post a Job</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Companies</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Career Advice</a>
          </li>
        </ul>

        <!-- Search Bar -->
        <form class="d-flex me-3">
          <input class="form-control me-2" type="search" placeholder="Search jobs, companies..." />
          <button class="btn btn-outline-light" type="submit">Search</button>
        </form>

        <!-- Profile & Auth Buttons -->
        <div class="d-flex align-items-center">
          <button class="btn btn-outline-light me-2">Login</button>
          <button class="btn btn-warning">Sign Up</button>

          <!-- Profile Dropdown -->
          <div class="dropdown ms-3">
            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
              <img src="@/assets/user.png" style="max-height: 30px;" alt="User" class="rounded-circle" />
            </button>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" href="#">Profile</a></li>
              <li><a class="dropdown-item" href="#">Saved Jobs</a></li>
              <li><a class="dropdown-item" href="#">Settings</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item text-danger" href="#">Logout</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar-brand {
  font-size: 1.5rem;
}
</style>

