<template>
  <div class="find-jobs-page">
    <div v-html="html"></div>
    <!--<div class="jobs-list">
      <div v-for="job in JobsJSON['items']" :key="'Job ID'" class="job-card">
        <h2>{{ job.title }}</h2>
        <p>{{ job.description }}</p>
      </div>
    </div>
    -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const jobs = ref([]);

  // CLIENT SIDE
const html = ref(null)

async function fetchOwnContent() {
  const url = 'https://npvdpxycgi.execute-api.us-east-2.amazonaws.com/dev/reading'
  try {
    const response = await fetch(url)
    const jsonResponse = await response.json()
    return jsonResponse
    // In Vue, you should avoid directly manipulating DOM with innerHTML
    // Instead, use v-html directive in your template
  } catch (error) {
    console.error('Error fetching content:', error);
  }
}

onMounted(() => {
  fetchOwnContent().then(result => {
    console.log(result)
    const JobsJSON = JSON.parse(JSON.stringify(result))
    for (let i = 0; i < JobsJSON.items.length; i++) {
      //console.log(i);
      console.log(JobsJSON["items"][i]);
      }
    return JobsJSON
  })
})

</script>


<style scoped>
.find-jobs-page {
  padding: 0rem;
}
.job-card {
  border: 1px solid #ddd;
  padding: 0rem;
  margin-bottom: 0rem;
  border-radius: 0.5rem;
}

</style>
