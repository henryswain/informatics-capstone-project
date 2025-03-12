<template>
  <div class="home-page">
    <div class="center-logo-area">
    <!--
      this is all very broken lol
      I will return another time to make it not broken though so just hold on
    -->
      <img 
        class = "home-page-logo"
        src="@/assets/CQ_logo.svg"
      />
      <br>
      <h4>Taking your job search to new heights</h4>
      <br>
      <!--
      in case we don't want the search stuff
      <div class="search-area">
        <form class="d-flex me-3" @submit.prevent="handleSubmit">
          <input
            class="form-control me-2"
            type="text"
            v-model="searchText"
            placeholder="Search jobs..."
            />
          <button class="btn search-button" type="text">Search</button>
        </form>
      </div>
      -->
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref, onMounted, defineProps, watch, computed } from 'vue';

const darkMode = ref(false);

const loadSettings = () => {
  const savedSettings = localStorage.getItem('userSettings');
  if (savedSettings) {
    const settings = JSON.parse(savedSettings);
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

watch(darkMode, applyDarkMode);

onMounted(() => {
  loadSettings();
  applyDarkMode();
});

</script>

<!-- Scoped style for homepage -->
<style scoped>
:global(body) {
  background-image: url("src/assets/home-page-bg-TEMP.jpg");
  background-repeat: no-repeat;
  background-size:cover;
  width: auto;
  height: auto;
}

.center-logo-area {
  
  margin-left: auto;
  margin-right: auto;
  top: 50%;
  bottom: 50%;
  text-align: center;
}

.home-page-logo {
  max-width: 1000px;
  vertical-align: middle;
  margin: auto;
  padding: 50px;
  fill: rgb(0, 0, 0);
}

.search-box {
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.search-button {
  fill :rgb(61, 67, 151);
}
</style>

<!-- Global dark mode overrides -->
<style>
.dark-mode {
  background-color: #121212;
  color: #ffffff;
}
</style>
