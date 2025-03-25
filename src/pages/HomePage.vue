<template>
  <div class="home-page">
    <br>
    <div class="center-logo-area">
      <img class = "home-page-logo"/>
      <br>
      <h4>Taking your job search to new heights</h4>
      <br>
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

.home-page {
  background-image: url("@/assets/bg_lightmode.png");
  background-repeat: no-repeat;
  background-size:cover;
  position:fixed;
  width: 100%;
  height: 100%;
  top: 50px;
  left: 0px;
  z-index: 1000;
}

.center-logo-area {
  backdrop-filter: blur(6px);
  margin-left: auto;
  margin-right: auto;
  max-width: 1000px;
  text-align: center;
  border-radius: 50px;
}

.home-page-logo {
  content: url("@/assets/CQ_logo_lightmode.svg");
  max-width: 1000px;
  padding: 50px;
}
</style>

<!-- Global dark mode overrides -->
<style>
.dark-mode {
  color: #ffffff;
}
.dark-mode .home-page {
  background-color: #121212;
  background-image: url("src/assets/bg_darkmode.png");
  background-repeat: no-repeat;
  background-size:cover;
}

.dark-mode .home-page-logo {
  content: url("@/assets/CQ_logo_darkmode.svg");
}

</style>
