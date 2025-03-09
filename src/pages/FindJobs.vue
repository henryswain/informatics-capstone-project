<template>
  <div class="find-jobs-page">
    <div v-for="item of items">
      <div class="card mb-3"><h5 class="card-header">{{ item["Civil Service Title"] }}</h5>
        <div class="card-body">
          <div v-if='item["Salary Frequency"] == "Hourly" && item["Full-Time/Part-Time indicator"] == "F"'>
            <p class="card-text">{{item["Salary Range From"]}} - {{item["Salary Range From"]}}/hr &#8226 Full-time</p>
          </div>
          <div v-else-if='item["Salary Frequency"] == "Hourly" && item["Full-Time/Part-Time indicator"] == "P"'>
            <p class="card-text">{{item["Salary Range From"]}} - {{item["Salary Range From"]}}/hr &#8226 Part-time</p>
          </div>
          <div v-else-if='item["Salary Frequency"] == "Annual" && item["Full-Time/Part-Time indicator"] == "F"'>
            <p class="card-text">{{item["Salary Range From"]}} - {{item["Salary Range From"]}}/yr &#8226 Full-time</p>
          </div>
          <div v-else-if='item["Salary Frequency"] == "Annual" && item["Full-Time/Part-Time indicator"] == "P"'>
            <p class="card-text">{{item["Salary Range From"]}} - {{item["Salary Range From"]}}/yr &#8226 Part-time</p>
          </div>
          <p class="card-text">Location: {{item["Work Location"]}}</p>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" :id='`button_${item["Job ID"]}`' :data-bs-target='`#modal_${item["Job ID"]}`'>
            Learn More
        </button>

        <!-- Modal -->
        <div class="modal fade" :id='`modal_${item["Job ID"]}`' tabindex="-1" aria-labelledby="more information" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                  <h1 class="modal-title fs-5" id="exampleModalLabel">{{ item["Civil Service Title"] }}</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                  <h5>Job Description</h5>
                  <p>{{item["Job Description"]}}</p>
                  <h5>Basic Qual Requirements</h5>
                  <p>{{item["Minimum Qual Requirements"]}}</p>
                  <h5>Preferred Skills</h5>
                  <p>{{ item["Preferred Skills"] }}</p>
                  <h5>To Apply</h5>
                  <p>{{ item["To Apply"] }}</p>
              
              </div>
              <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
        </div>
        </div></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref, onMounted, defineProps, watch } from 'vue';
const props = defineProps({
  query: String
})
const route = useRoute();

const jobs = ref([]);
const query = ref(props.query);

// 

// To this:
watch(() => props.query, (newQueryString, oldQueryString) => {
  if (newQueryString) {
    fetchJobs({searchQuery: newQueryString})
  }
  else {
    fetchJobs()
  }
});

  // CLIENT SIDE
const html = ref(null)

const items = ref([]);


async function fetchJobs({ pageToken = null, searchQuery = null } = {}) {
  items.value = []
  const fetchData = async (url) => {
    try {
      const result = await fetch(url);
      const response = await result.json();
      items.value = [...items.value, ...response.items];
      return encodeURIComponent(response.nextPageToken);
    } catch (error) {
      console.error("Error fetching data:", error);
      return null;
    }
  };

  let url = "https://npvdpxycgi.execute-api.us-east-2.amazonaws.com/dev2/reading";
  if (pageToken) url += `?pageToken=${encodeURIComponent(pageToken)}`;
  if (searchQuery) url += `${pageToken ? '&' : '?'}search=${searchQuery}`;

  let nextPageToken = await fetchData(url);
  while (nextPageToken && nextPageToken !== "undefined") {
    url = `https://npvdpxycgi.execute-api.us-east-2.amazonaws.com/dev2/reading?pageToken=${nextPageToken}`;
    if (searchQuery) url += `&search=${searchQuery}`;
    nextPageToken = await fetchData(url);
  }
  return
}


onMounted(() => {
  if (props.query) {
    fetchJobs({searchQuery: props.query});
  }
  else {
    fetchJobs()
  }
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
