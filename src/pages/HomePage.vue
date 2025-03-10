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
      <h1>Yada yada tagline here</h1>
      <form class="d-flex me-3" @submit.prevent="handleSubmit">
        <input
          class="form-control me-2"
          type="text"
          v-model="searchText"
          placeholder="Search jobs..."
          />
        <button class="btn btn-outline-light" type="text">Search</button>
      </form>
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
.home-page-logo {
  max-width: 100;
  margin: auto;
  fill: rgb(0, 0, 0);
}
</style>

<!-- Global dark mode overrides -->
<style>
.dark-mode {
  background-color: #121212;
  color: #ffffff;
}
</style>
