<template>
  <div class="find-jobs-page">
    <h1 class="mb-4">Find Jobs</h1>
    <div v-html="html"></div>
    <!-- <div class="jobs-list">
      <div v-for="job in jobs" :key="job.id" class="job-card">
        <h2>{{ job.title }}</h2>
        <p>{{ job.description }}</p>
      </div>
    </div> -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const jobs = ref([]);

// onMounted(() => {
//   this is just for show. we will replace it with the API call later
//   jobs.value = [
//     { id: 1, title: 'Software Engineer', description: 'Be an engineer of the software.' },
//     { id: 2, title: 'Product Manager', description: 'Be a manager of thee ole product.' },
//     { id: 3, title: 'UX Designer', description: 'Be a designer of thee ole Ux.' },
//   ];
// })

  // CLIENT SIDE
const html = ref(null)

async function fetchOwnContent() {
  try {
    const response = await fetch('https://webdev.divms.uiowa.edu/webdev/cs3910/henryswain/informatics-capstone-project/jobview.wsgi')
    const text = await response.text()  // Use .text() instead of .html
    html.value = text
    
    // In Vue, you should avoid directly manipulating DOM with innerHTML
    // Instead, use v-html directive in your template
  } catch (error) {
    console.error('Error fetching content:', error);
  }
}


onMounted(() => {
  fetchOwnContent()
})

</script>

<style scoped>
.find-jobs-page {
  padding: 2rem;
}
.job-card {
  border: 1px solid #ddd;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 0.5rem;
}
</style>
