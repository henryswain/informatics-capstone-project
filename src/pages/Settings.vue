<script setup>
import { ref, watch, onMounted } from 'vue';

// Load settings
const loadSettings = () => {
  const savedSettings = localStorage.getItem('userSettings');
  return savedSettings ? JSON.parse(savedSettings) : {
    itemsPerPage: 10,
    darkMode: false
  };
};

const settings = ref(loadSettings());

watch(settings, (newVal) => {
  localStorage.setItem('userSettings', JSON.stringify(newVal));
}, { deep: true });

// Apply dark mode
const applyDarkMode = () => {
  if (settings.value.darkMode) {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
};

onMounted(() => {
  applyDarkMode();
});

watch(() => settings.value.darkMode, applyDarkMode);

// Clear local storage
const clearLocalStorage = () => {
  localStorage.clear();
  alert('Local storage cleared.');
  // Reload to default
  settings.value = { itemsPerPage: 10, darkMode: false };
};
</script>

<template>
  <div class="settings-container">
    <h2>Settings</h2>

    <div class="setting-group">
      <label for="itemsPerPage">Jobs Per Page:</label>
      <select id="itemsPerPage" v-model="settings.itemsPerPage">
        <option v-for="num in [5, 10, 20, 50]" :key="num" :value="num">
          {{ num }}
        </option>
      </select>
    </div>

    <div class="setting-group">
      <label for="darkMode">Dark Mode:</label>
      <input id="darkMode" type="checkbox" v-model="settings.darkMode" />
    </div>

    <button class="btn btn-danger" @click="clearLocalStorage">
      Clear Local Storage
    </button>
  </div>
</template>

<style scoped>
.settings-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.setting-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 15px 0;
}

label {
  font-size: 1.1em;
}

select, input[type="checkbox"] {
  font-size: 1em;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
  padding: 10px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  width: 100%;
  margin-top: 20px;
}

.dark-mode {
  background-color: #121212;
  color: #ffffff;
}
.dark-mode .settings-container {
  background: #333;
  color: #fff;
}
</style>
