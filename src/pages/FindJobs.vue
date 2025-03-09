<template>
  <div class="find-jobs-page">
    <div v-for="item of paginatedItems" :key="item['Job ID']">
      <div class="card mb-3">
        <h5 class="card-header">{{ item["Civil Service Title"] }}</h5>
        <div class="card-body">
          <div v-if='item["Salary Frequency"] == "Hourly" && item["Full-Time/Part-Time indicator"] == "F"'>
            <p class="card-text">{{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/hr • Full-time</p>
          </div>
          <div v-else-if='item["Salary Frequency"] == "Hourly" && item["Full-Time/Part-Time indicator"] == "P"'>
            <p class="card-text">{{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/hr • Part-time</p>
          </div>
          <div v-else-if='item["Salary Frequency"] == "Annual" && item["Full-Time/Part-Time indicator"] == "F"'>
            <p class="card-text">{{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/yr • Full-time</p>
          </div>
          <div v-else-if='item["Salary Frequency"] == "Annual" && item["Full-Time/Part-Time indicator"] == "P"'>
            <p class="card-text">{{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/yr • Part-time</p>
          </div>
          <p class="card-text">Location: {{ item["Work Location"] }}</p>

          <!-- Action Buttons -->
          <div class="btn-group">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" :id='`button_${item["Job ID"]}`' :data-bs-target='`#modal_${item["Job ID"]}`'>
              Learn More
            </button>
            <button type="button" class="btn btn-success ms-2" @click="saveJob(item)">
              {{ isJobSaved(item["Job ID"]) ? "Saved" : "Save Job" }}
            </button>
          </div>

          <!-- Modal -->
          <div class="modal fade" :id='`modal_${item["Job ID"]}`' tabindex="-1" aria-labelledby="more information" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h1 class="modal-title fs-5">{{ item["Civil Service Title"] }}</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <h5>Job Description</h5>
                  <p>{{ item["Job Description"] }}</p>
                  <h5>Basic Qual Requirements</h5>
                  <p>{{ item["Minimum Qual Requirements"] }}</p>
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
          </div>

        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div class="pagination-controls">
      <button class="btn btn-secondary" @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }}</span>
      <button class="btn btn-secondary" @click="nextPage" :disabled="currentPage * itemsPerPage >= items.length">Next</button>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref, onMounted, defineProps, watch, computed } from 'vue';

const props = defineProps({
  query: String
});
const route = useRoute();
const jobs = ref([]);
const query = ref(props.query);
const items = ref([]);

// Load saved jobs from localStorage
const savedJobs = ref(JSON.parse(localStorage.getItem('savedJobs')) || []);

function saveJob(job) {
  if (!isJobSaved(job["Job ID"])) {
    savedJobs.value.push({
      id: job["Job ID"],
      title: job["Civil Service Title"],
      company: job["Agency"],
      location: job["Work Location"]
    });
    localStorage.setItem('savedJobs', JSON.stringify(savedJobs.value));
  }
}

// Check if a job is already saved
function isJobSaved(jobId) {
  return savedJobs.value.some(job => job.id === jobId);
}

// Load settings
const itemsPerPage = ref(10);
const currentPage = ref(1);
const darkMode = ref(false);

const loadSettings = () => {
  const savedSettings = localStorage.getItem('userSettings');
  if (savedSettings) {
    const settings = JSON.parse(savedSettings);
    itemsPerPage.value = settings.itemsPerPage || 10;
    darkMode.value = settings.darkMode || false;
  }
};

// Apply dark mode 
const applyDarkMode = () => {
  if (darkMode.value) {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
};

// Fetch jobs
async function fetchJobs({ pageToken = null, searchQuery = null } = {}) {
  items.value = [];
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
}

// Paginate
const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return items.value.slice(start, end);
});

const nextPage = () => {
  if (currentPage.value * itemsPerPage.value < items.value.length) {
    currentPage.value++;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

watch(() => props.query, (newQueryString) => {
  if (newQueryString) {
    fetchJobs({ searchQuery: newQueryString });
  } else {
    fetchJobs();
  }
});

// Dark Mode
watch(darkMode, applyDarkMode);

onMounted(() => {
  loadSettings();
  applyDarkMode();
  if (props.query) {
    fetchJobs({ searchQuery: props.query });
  } else {
    fetchJobs();
  }
});
</script>

<style scoped>
.find-jobs-page {
  padding: 1rem;
}

.card {
  border: 1px solid #ddd;
  border-radius: 0.5rem;
}

.pagination-controls {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.dark-mode {
  background-color: #121212;
  color: white;
}

.dark-mode .card {
  background: #333;
  color: white;
}
</style>
