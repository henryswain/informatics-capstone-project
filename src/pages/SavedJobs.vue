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
        
        <div class="btn-group">
          <!-- Learn More -->
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#modal_' + job.id">
            Learn More
          </button>

          <!-- Remove -->
          <button class="btn btn-danger ms-2" @click="removeJob(job.id)">Remove</button>
        </div>

        <!-- Description Modal -->
        <div class="modal fade" :id="'modal_' + job.id" tabindex="-1" aria-labelledby="more information" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5">{{ job.title }}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <h5>Company</h5>
                <h5>Location</h5>
                <h5>Job Description</h5>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>

      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

// Load saved jobs
const loadSavedJobs = () => {
  const storedJobs = localStorage.getItem('savedJobs');
  return storedJobs ? JSON.parse(storedJobs) : [];
};

const savedJobs = ref(loadSavedJobs());

watch(savedJobs, (newJobs) => {
  localStorage.setItem('savedJobs', JSON.stringify(newJobs));
}, { deep: true });

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

.btn-group {
  display: flex;
  gap: 10px;
}
</style>
