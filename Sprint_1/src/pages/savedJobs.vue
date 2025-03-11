<template>
  <div class="saved-jobs-container">
    <h1>Saved Jobs</h1>
    <div v-if="savedJobs.length === 0" class="no-jobs">
      <p>No Jobs Saved</p>
    </div>
    <ul v-else class="jobs-list">
      <li v-for="job in savedJobs" :key="job.id" class="job-item">
        <h3>{{ job.title }}</h3>
        <p>{{ job.company }}</p>
        <p><strong>Location:</strong> {{ job.location }}</p>
        <button class="btn btn-danger" @click="removeJob(job.id)">Remove</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const savedJobs = ref([
  { id: 1, title: "Example Job", company: "Example Company", location: "Example Location" },
]);

function removeJob(id) {
  savedJobs.value = savedJobs.value.filter(job => job.id !== id);
}
</script>

<style scoped>
.saved-jobs-container {
  padding: 2rem;
}

.no-jobs {
  text-align: center;
  color: #777;
}

.jobs-list {
  list-style: none;
  padding: 0;
}

.job-item {
  border: 1px solid #ddd;
  padding: 1rem;
  margin-bottom: 1rem;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
