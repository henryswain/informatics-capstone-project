<template>
  <div class="find-jobs-page">
    <div class="grid-container">
      <!-- Filter Section -->
      <div class="filter-section">
        <div class="card filter-card mb-4">
          <div class="card-body">
            <h5 class="card-title">Filter Your Search</h5>

            <!-- Job Type Filter -->
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

            <!-- Job Category Filter -->
            <div class="filter-group mt-3">
              <h6>Job Category</h6>
              <div class="filter-options">
                <button
                  v-for="option in jobCategoryOptions"
                  :key="option"
                  :class="['filter-box', { active: filters.industries.includes(option) }]"
                  @click="toggleFilter('industries', option)"
                >
                  {{ option }}
                </button>
              </div>
            </div>

            <!-- Career Level Filter -->
            <div class="filter-group mt-3">
              <h6>Career Level</h6>
              <div class="filter-options">
                <button
                  v-for="option in careerLevelOptions"
                  :key="option"
                  :class="['filter-box', { active: filters.careerLevels.includes(option) }]"
                  @click="toggleFilter('careerLevels', option)"
                >
                  {{ option }}
                </button>
              </div>
            </div>

            <!-- Location Filter -->
            <div class="filter-group mt-3">
              <h6>Location</h6>
              <input
                type="text"
                class="form-control"
                placeholder="Enter city or zip"
                v-model="filters.location"
              />
            </div>

            <!-- Apply Filters -->
            <button class="btn btn-primary w-100 mt-3" @click="applyFilters">
              Apply Filters
            </button>
          </div>
        </div>
      </div>

      <!-- Jobs Section -->
      <div class="jobs-section">
        <div v-if="paginatedItems.length === 0">
          <p>No matching jobs found.</p>
        </div>
        <div v-else>
          <div
            v-for="(item, index) in paginatedItems"
            :key="item['Job ID']"
            class="card mb-3"
          >
            <h5 class="card-header">{{ item["Civil Service Title"] }}</h5>
            <div class="card-body">
              <!-- Salary Frequency / FT/PT logic -->
              <div
                v-if='item["Salary Frequency"] === "Hourly" && item["Full-Time/Part-Time indicator"] === "F"'
              >
                <p class="card-text">
                  {{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/hr • Full-time
                </p>
              </div>
              <div
                v-else-if='item["Salary Frequency"] === "Hourly" && item["Full-Time/Part-Time indicator"] === "P"'
              >
                <p class="card-text">
                  {{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/hr • Part-time
                </p>
              </div>
              <div
                v-else-if='item["Salary Frequency"] === "Annual" && item["Full-Time/Part-Time indicator"] === "F"'
              >
                <p class="card-text">
                  {{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/yr • Full-time
                </p>
              </div>
              <div
                v-else-if='item["Salary Frequency"] === "Annual" && item["Full-Time/Part-Time indicator"] === "P"'
              >
                <p class="card-text">
                  {{ item["Salary Range From"] }} - {{ item["Salary Range From"] }}/yr • Part-time
                </p>
              </div>
              <p class="card-text">Location: {{ item["Work Location"] }}</p>

              <!-- Action Buttons -->
              <div class="btn-group">
                <button
                  type="button"
                  class="btn btn-primary"
                  data-bs-toggle="modal"
                  :id="`button_${item['Job ID']}`"
                  :data-bs-target="`#modal_${item['Job ID']}`"
                >
                  Learn More
                </button>
                <button
                  type="button"
                  :class="isJobSaved(item['Job ID']) ? 'btn btn-danger ms-2' : 'btn btn-success ms-2'"
                  @click="toggleJob(item)"
                >
                  {{ isJobSaved(item["Job ID"]) ? "Remove Job" : "Save Job" }}
                </button>

              </div>

              <!-- Modal -->
              <div
                class="modal fade"
                :id="`modal_${item['Job ID']}`"
                tabindex="-1"
                aria-hidden="true"
              >
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h1 class="modal-title fs-5">
                        {{ item["Civil Service Title"] }}
                      </h1>
                      <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                      ></button>
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
                      <button
                        type="button"
                        class="btn btn-secondary"
                        data-bs-dismiss="modal"
                      >
                        Close
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <!-- End Modal -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div class="pagination-controls">
      <button class="btn btn-secondary" @click="prevPage" :disabled="currentPage === 1">
        Previous
      </button>
      <span>Page {{ currentPage }}</span>
      <button
        class="btn btn-secondary"
        @click="nextPage"
        :disabled="currentPage * itemsPerPage >= filteredJobs.length"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps, watch, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import Papa from "papaparse";
import jobsCsv from "@/assets/Jobs_NYC_Postings.csv?raw";

const props = defineProps({
  query: String,
});

const route = useRoute();
const router = useRouter();

const allJobs = ref([]);
const filteredJobs = ref([]);
const currentPage = ref(1);
const itemsPerPage = ref(10);

// const searchText = ref(props.query || "");

// For saved jobs
const savedJobs = ref(JSON.parse(localStorage.getItem("savedJobs")) || []);

function saveJob(job) {
  if (!isJobSaved(job["Job ID"])) {
    savedJobs.value.push({
      id: job["Job ID"],
      title: job["Civil Service Title"],
      company: job["Agency"],
      location: job["Work Location"],
    });
    localStorage.setItem("savedJobs", JSON.stringify(savedJobs.value));
  }
}

function removeJob(jobId) {
  savedJobs.value = savedJobs.value.filter(job => job.id !== jobId);
  localStorage.setItem("savedJobs", JSON.stringify(savedJobs.value));
}

function toggleJob(job) {
  if (isJobSaved(job["Job ID"])) {
    removeJob(job["Job ID"]);
  } else {
    saveJob(job);
  }
}

function isJobSaved(jobId) {
  return savedJobs.value.some(job => job.id === jobId);
}

// Parse CSV on mount
onMounted(() => {
  Papa.parse(jobsCsv, {
    header: true,
    skipEmptyLines: true,
    complete: (results) => {
      allJobs.value = results.data;
      filteredJobs.value = results.data;
    },
  });
});

// Pagination
const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  return filteredJobs.value.slice(start, start + itemsPerPage.value);
});

function nextPage() {
  if (currentPage.value * itemsPerPage.value < filteredJobs.value.length) {
    currentPage.value++;
  }
}

function prevPage() {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
}

// Filter arrays
const jobTypeOptions = ["Full-Time", "Part-Time"];
const jobCategoryOptions = [
  // Add whichever categories you want the user to select
  "Engineering, Architecture, & Planning",
  "Health",
  "Public Safety, Inspections, & Enforcement",
  // ...
];
const careerLevelOptions = [
  "Entry-Level",
  "Experienced (non-manager)",
  "Manager",
  "Student",
];

// Filter object
const filters = ref({
  jobTypes: [],
  industries: [],
  careerLevels: [],
  location: "",
  searchText: props.query || ""
});

// Toggle a filter
function toggleFilter(filterCategory, option) {
  const index = filters.value[filterCategory].indexOf(option);
  if (index === -1) {
    filters.value[filterCategory].push(option);
  } else {
    filters.value[filterCategory].splice(index, 1);
  }
}

// Apply filter logic
function applyFilters(newQueryString = "") {
  let results = [...allJobs.value];

  // Convert "Full-Time"/"Part-Time" to "F"/"P"
  const mapJobType = {
    "Full-Time": "F",
    "Part-Time": "P",
  };

  // 1) Full-Time/Part-Time
  if (filters.value.jobTypes.length > 0) {
    results = results.filter((job) => {
      const csvVal = job["Full-Time/Part-Time indicator"]; // "F" or "P"
      return filters.value.jobTypes.some((selected) => {
        return csvVal === mapJobType[selected];
      });
    });
  }

  // 2) Job Category (substring match)
  if (filters.value.industries.length > 0) {
    results = results.filter((job) => {
      const catStr = job["Job Category"] || "";
      return filters.value.industries.some((selectedCat) =>
        catStr.includes(selectedCat)
      );
    });
  }

  // 3) Career Level (needs to be exact)
  if (filters.value.careerLevels.length > 0) {
    results = results.filter((job) =>
      filters.value.careerLevels.includes(job["Career Level"])
    );
  }

  // 4) Location (partial match)
  if (filters.value.location.trim()) {
    const loc = filters.value.location.toLowerCase();
    results = results.filter((job) =>
      job["Work Location"]?.toLowerCase()?.includes(loc)
    );
  }

  if (newQueryString.length > 0) {
    // console.log("filters.value.searchText.length > 0: ", filters.value.searchText)
    // const searchText2 = filters.value.searchText.toLowerCase();
    const newString = newQueryString.toLowerCase()
    results = results.filter((job) => {
      if (job["Civil Service Title"]?.toLowerCase()?.includes(newString) || job["Job Description"]?.toLowerCase()?.includes(newString) || job["Minimum Qual Requirements"]?.toLowerCase()?.includes(newString) || job["Preferred Skills"]?.toLowerCase().includes(newString)) {
        return true
      }
    });
  }


  filteredJobs.value = results;
  currentPage.value = 1;
}

// If user changes query param, re-run filters or revert
watch(
  () => props.query,
  (newQueryString) => {
    console.log("watch called")
    if (newQueryString) {
      console.log("newQueryString: ", newQueryString)
      console.log("inside if statement")
      applyFilters(newQueryString);
    } else {
      console.log("inside else statement")
      filteredJobs.value = [...allJobs.value];
    }
  }
);
</script>

<style scoped>
.find-jobs-page {
  padding: 1rem;
}
.grid-container {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 20px;
  padding: 1rem;
}
.filter-section {
  padding: 1rem;
  background-color: #f5f7fa;
  border-right: 1px solid #ddd;
}
.jobs-section {
  padding: 1rem;
}
.pagination-controls {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}
.card {
  border: 1px solid #ddd;
  border-radius: 0.5rem;
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
@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: 1fr;
  }
}
</style>

<style>
.modal {
  z-index: 2100 !important;
}
.modal-backdrop {
  z-index: 2050 !important;
}
.modal-dialog {
  margin-top: 80px;
}
.dark-mode .form-control,
.dark-mode input[type="text"],
.dark-mode input[type="email"],
.dark-mode input[type="search"],
.dark-mode input[type="password"],
.dark-mode select,
.dark-mode textarea,
.dark-mode .form-control {
  background-color: #444444 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .form-control::placeholder,
.dark-mode input[type="text"]::placeholder,
.dark-mode input[type="email"]::placeholder,
.dark-mode input[type="search"]::placeholder,
.dark-mode input[type="password"]::placeholder,
.dark-mode select::placeholder,
.dark-mode textarea::placeholder,
.dark-mode .form-control::placeholder {
  color: #cccccc !important;
}
.dark-mode .modal-content,
.dark-mode .modal-header,
.dark-mode .modal-body,
.dark-mode .modal-footer {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .btn-close {
  filter: invert(1);
}
.dark-mode .filter-section,
.dark-mode .filter-section * {
  background-color: #333333 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .filter-card {
  background-color: #444444 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .filter-box {
  background-color: #444444 !important;
  color: #ffffff !important;
  border-color: #555555 !important;
}
.dark-mode .filter-box.active {
  background-color: #007bff !important;
  color: #ffffff !important;
  border-color: #007bff !important;
}
</style>
