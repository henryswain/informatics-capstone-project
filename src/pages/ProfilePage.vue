<script setup>
import { ref, watch, onMounted } from 'vue';

// Load profile data from localStorage
const loadProfile = () => {
  const savedProfile = localStorage.getItem('userProfile');
  return savedProfile ? JSON.parse(savedProfile) : {
    name: "Your Name",
    headline: "Your Professional Headline",
    email: "youremail@example.com",
    location: "Your Location",
    profilePicture: "", 
    about: "A short summary about your professional background.",
    experience: [],
    education: [],
    skills: [],
    qualifications: []
  };
};

const user = ref(loadProfile());
const isEditing = ref(false);
const newSkill = ref("");
const newQualification = ref("");
const newExperience = ref({ position: "", company: "", duration: "" });
const newEducation = ref({ degree: "", institution: "", year: "" });

// Watch and save changes to localStorage
watch(user, (newVal) => {
  localStorage.setItem('userProfile', JSON.stringify(newVal));
}, { deep: true });

// Save the profile and stop editing
const saveProfile = () => {
  isEditing.value = false;
  console.log("Profile updated:", user.value);
};

// Add skill, qualification, experience, and education
const addSkill = () => {
  if (newSkill.value.trim()) {
    user.value.skills.push(newSkill.value.trim());
    newSkill.value = "";
  }
};

const addQualification = () => {
  if (newQualification.value.trim()) {
    user.value.qualifications.push(newQualification.value.trim());
    newQualification.value = "";
  }
};

const addExperience = () => {
  if (newExperience.value.position && newExperience.value.company && newExperience.value.duration) {
    user.value.experience.push({ ...newExperience.value });
    newExperience.value = { position: "", company: "", duration: "" };
  }
};

const addEducation = () => {
  if (newEducation.value.degree && newEducation.value.institution && newEducation.value.year) {
    user.value.education.push({ ...newEducation.value });
    newEducation.value = { degree: "", institution: "", year: "" };
  }
};

// Handle profile picture upload
const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      user.value.profilePicture = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};

import { getCurrentUser } from 'aws-amplify/auth';

import { Hub } from 'aws-amplify/utils';

Hub.listen('auth', async({ payload }) => {
  console.log("Hub.listen called")
  getUserInformation()
})
const currentUserInfo = ref({})
onMounted(async() => {
 getUserInformation()
})
const getUserInformation = async () => {
  try {
  const { username, userId, signInDetails } = await getCurrentUser();
  currentUserInfo.value = {username: username,  userId: userId, signInDetails: signInDetails}
  }
  catch (e) {
    console.log(e.message)
    currentUserInfo.value = {username: undefined, userId: undefined, signInDetails: undefined}
  }
}
// Delete experience, education, or qualification
const deleteItem = (array, index) => {
  array.splice(index, 1);
};
</script>

<template>
  <div class="profile-container">
    <!-- Profile Header -->
    <div class="profile-header">
      <h5>username: {{currentUserInfo.username}}</h5>
      <h5>userId: {{currentUserInfo.userId}}</h5>
      <h5>signInDetails: {{currentUserInfo.signInDetails}}</h5>

      <div class="profile-picture-container">
        <label class="profile-upload">
          <input type="file" @change="handleFileUpload" hidden />
          <img :src="user.profilePicture || '/user.png'" alt="Profile Picture" class="profile-picture" />
        </label>
        <button @click="handleFileUpload" class="btn btn-upload">Change Profile Picture</button>
      </div>
      <template v-if="isEditing">
        <input v-model="user.name" class="input-field" placeholder="Enter Name" />
        <input v-model="user.headline" class="input-field" placeholder="Enter Headline" />
      </template>
      <template v-else>
        <h2>{{ user.name }}</h2>
        <p class="headline">{{ user.headline }}</p>
      </template>
    </div>

    <!-- Profile Details Section -->
    <div class="profile-details">
      <h3>About</h3>
      <template v-if="isEditing">
        <textarea v-model="user.about" class="input-field" placeholder="Enter About"></textarea>
      </template>
      <template v-else>
        <p>{{ user.about }}</p>
      </template>

      <h3>Experience</h3>
      <ul>
        <li v-for="(job, index) in user.experience" :key="index">
          <strong>{{ job.position }}</strong> at {{ job.company }} ({{ job.duration }})
          <button v-if="isEditing" @click="deleteItem(user.experience, index)" class="btn btn-delete">Delete</button>
        </li>
      </ul>
      <template v-if="isEditing">
        <input v-model="newExperience.position" class="input-field" placeholder="Position" />
        <input v-model="newExperience.company" class="input-field" placeholder="Company" />
        <input v-model="newExperience.duration" class="input-field" placeholder="Duration" />
        <button class="btn btn-secondary" @click="addExperience">Add Experience</button>
      </template>

      <h3>Education</h3>
      <ul>
        <li v-for="(edu, index) in user.education" :key="index">
          <strong>{{ edu.degree }}</strong> - {{ edu.institution }} ({{ edu.year }})
          <button v-if="isEditing" @click="deleteItem(user.education, index)" class="btn btn-delete">Delete</button>
        </li>
      </ul>
      <template v-if="isEditing">
        <input v-model="newEducation.degree" class="input-field" placeholder="Degree" />
        <input v-model="newEducation.institution" class="input-field" placeholder="Institution" />
        <input v-model="newEducation.year" class="input-field" placeholder="Year" />
        <button class="btn btn-secondary" @click="addEducation">Add Education</button>
      </template>

      <h3>Skills</h3>
      <ul>
        <li v-for="(skill, index) in user.skills" :key="index">
          <input type="checkbox" :checked="true" /> {{ skill }}
        </li>
      </ul>
      <template v-if="isEditing">
        <input v-model="newSkill" class="input-field" placeholder="Enter Skill" />
        <button class="btn btn-secondary" @click="addSkill">Add Skill</button>
      </template>

      <h3>Qualifications</h3>
      <ul>
        <li v-for="(qualification, index) in user.qualifications" :key="index">
          <input type="checkbox" :checked="true" /> {{ qualification }}
          <button v-if="isEditing" @click="deleteItem(user.qualifications, index)" class="btn btn-delete">Delete</button>
        </li>
      </ul>
      <template v-if="isEditing">
        <input v-model="newQualification" class="input-field" placeholder="Enter Qualification" />
        <button class="btn btn-secondary" @click="addQualification">Add Qualification</button>
      </template>
    </div>

    <!-- Action Buttons -->
    <div class="profile-actions">
      <button v-if="!isEditing" class="btn btn-primary" @click="isEditing = true">Edit Profile</button>
      <button v-else class="btn btn-success" @click="saveProfile">Save</button>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.profile-header {
  text-align: center;
}

.profile-picture-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.profile-upload {
  display: inline-block;
  cursor: pointer;
}

.profile-picture {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 2px solid #ddd;
}

.btn-upload {
  background-color: #0073b1;
  color: white;
  padding: 8px 16px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

.input-field {
  width: 100%;
  padding: 8px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn-primary {
  background-color: #0073b1;
  color: white;
}

.btn-success {
  background-color: #28a745;
  color: white;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
}

.btn-delete {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  margin-left: 10px;
}

.profile-details h3 {
  font-size: 1.2em;
  margin-top: 20px;
}

.profile-actions {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}
</style>
