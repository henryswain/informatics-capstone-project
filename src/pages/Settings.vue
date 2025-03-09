<template>
  <div class="settings-page container mt-4">
    <h1>Settings</h1>
    
    <!-- Appearance Section -->
    <section class="settings-section">
      <h2>Appearance</h2>
      <div class="setting-group">
        <label for="darkModeToggle">Dark Mode:</label>
        <input id="darkModeToggle" type="checkbox" v-model="settings.darkMode" />
        <span>{{ settings.darkMode ? 'Enabled' : 'Disabled' }}</span>
      </div>
      <div class="setting-group">
        <label for="fontSizeRange">Font Size: {{ settings.fontSize }}%</label>
        <input
          id="fontSizeRange"
          type="range"
          min="80"
          max="150"
          step="5"
          v-model="settings.fontSize"
          @input="updateFontSize"
        />
      </div>
    </section>
    
    <!-- Job Settings Section -->
    <section class="settings-section">
      <h2>Job Settings</h2>
      <div class="setting-group">
        <label for="itemsPerPage">Jobs Per Page:</label>
        <select id="itemsPerPage" v-model="settings.itemsPerPage">
          <option v-for="num in [5, 10, 20, 50]" :key="num" :value="num">
            {{ num }}
          </option>
        </select>
      </div>
    </section>
    
    <!-- Notifications Section -->
    <section class="settings-section">
      <h2>Notifications</h2>
      <div class="setting-group">
        <label for="emailNotifications">Email Notifications:</label>
        <input id="emailNotifications" type="checkbox" v-model="settings.emailNotifications" />
        <span>{{ settings.emailNotifications ? 'Enabled' : 'Disabled' }}</span>
      </div>
      <div class="setting-group">
        <label for="pushNotifications">Push Notifications:</label>
        <input id="pushNotifications" type="checkbox" v-model="settings.pushNotifications" />
        <span>{{ settings.pushNotifications ? 'Enabled' : 'Disabled' }}</span>
      </div>
    </section>
    
    <!-- Language & Accessibility Section -->
    <section class="settings-section">
      <h2>Language & Accessibility</h2>
      <div class="setting-group">
        <label for="languageSelect">Language:</label>
        <select id="languageSelect" v-model="settings.language">
          <option value="en">English</option>
          <option value="es">Español</option>
          <option value="fr">Français</option>
          <!-- Add more languages if needed -->
        </select>
      </div>
    </section>
    
    <!-- Reset Section -->
    <section class="settings-section">
      <h2>Reset</h2>
      <button class="btn btn-danger" @click="resetSettings">
        Reset to Defaults
      </button>
    </section>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';

// Define default settings
const defaultSettings = {
  darkMode: false,
  fontSize: 100,
  itemsPerPage: 10,
  emailNotifications: false,
  pushNotifications: false,
  language: 'en'
};

// Load settings from localStorage (or use defaults)
const loadSettings = () => {
  const savedSettings = localStorage.getItem('userSettings');
  return savedSettings ? JSON.parse(savedSettings) : defaultSettings;
};

const settings = ref(loadSettings());

// Persist settings changes in localStorage
watch(settings, (newVal) => {
  localStorage.setItem('userSettings', JSON.stringify(newVal));
}, { deep: true });

// Apply dark mode by toggling a class on document body
const applyDarkMode = () => {
  if (settings.value.darkMode) {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
};

onMounted(() => {
  applyDarkMode();
  updateFontSize();
});

// Watch dark mode setting changes
watch(() => settings.value.darkMode, applyDarkMode);

// Update the root font size for accessibility
const updateFontSize = () => {
  document.documentElement.style.fontSize = settings.value.fontSize + '%';
};

// Reset settings to defaults and clear localStorage
const resetSettings = () => {
  localStorage.clear();
  alert('Settings reset to defaults.');
  settings.value = { ...defaultSettings };
  applyDarkMode();
  updateFontSize();
};
</script>

<!-- Scoped styles for the settings page layout -->
<style scoped>
.settings-page {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.settings-section {
  margin-bottom: 2rem;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #f9f9f9;
}

.setting-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 15px 0;
}

label {
  font-size: 1.1em;
  margin-right: 10px;
}

select,
input[type="checkbox"],
input[type="range"] {
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
</style>

<!-- Global dark mode overrides -->
<style>
.dark-mode {
  background-color: #121212;
  color: #ffffff;
}

.dark-mode .settings-page {
  background: #333333;
  color: #ffffff;
}

.dark-mode .settings-section {
  background: #444444;
  border-color: #555555;
}

.dark-mode label,
.dark-mode select,
.dark-mode input,
.dark-mode button,
.dark-mode span {
  color: #ffffff !important;
}
.dark-mode .btn-danger {
  background-color: #b02a37;
}
</style>
