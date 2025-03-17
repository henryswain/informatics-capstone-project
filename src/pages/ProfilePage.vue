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
    qualifications: [],
    socialLinks: {
      twitter: "",
      linkedin: "",
      github: "",
      website: ""
    }
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
<<<<<<< HEAD
    <div class="profile-layout">
      <!-- Profile Section (View Mode) -->
      <div class="profile-view">
        <div class="profile-header">
          <div class="profile-picture-container">
            <label class="profile-upload">
              <input type="file" @change="handleFileUpload" hidden />
              <img :src="user.profilePicture || '/user.png'" alt="Profile Picture" class="profile-picture" />
            </label>
          </div>
          <h2>{{ user.name }}</h2>
          <p class="headline">{{ user.headline }}</p>
          <p>{{ user.about }}</p>
        </div>

        <div class="profile-sections">
          <div class="profile-section">
            <h3>Experience</h3>
            <ul>
              <li v-for="(job, index) in user.experience" :key="index">
                <strong>{{ job.position }}</strong> at {{ job.company }} ({{ job.duration }})
              </li>
            </ul>
          </div>

          <div class="profile-section">
            <h3>Education</h3>
            <ul>
              <li v-for="(edu, index) in user.education" :key="index">
                <strong>{{ edu.degree }}</strong> - {{ edu.institution }} ({{ edu.year }})
              </li>
            </ul>
          </div>

          <div class="profile-section">
            <h3>Skills</h3>
            <ul>
              <li v-for="(skill, index) in user.skills" :key="index">
                <input type="checkbox" :checked="true" /> {{ skill }}
              </li>
            </ul>
          </div>

          <!-- Social Media Links -->
          <div class="profile-section" v-if="user.socialLinks.twitter || user.socialLinks.linkedin || user.socialLinks.github || user.socialLinks.website">
            <h3>Social Links</h3>
            <ul>
              <li v-if="user.socialLinks.twitter">
                <a :href="user.socialLinks.twitter" target="_blank">Twitter</a>
              </li>
              <li v-if="user.socialLinks.linkedin">
                <a :href="user.socialLinks.linkedin" target="_blank">LinkedIn</a>
              </li>
              <li v-if="user.socialLinks.github">
                <a :href="user.socialLinks.github" target="_blank">GitHub</a>
              </li>
              <li v-if="user.socialLinks.website">
                <a :href="user.socialLinks.website" target="_blank">Website</a>
              </li>
            </ul>
          </div>
        </div>

        <div class="profile-actions">
          <button v-if="!isEditing" class="btn btn-primary" @click="isEditing = true">Edit Profile</button>
        </div>
=======
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
>>>>>>> c28c7196c94ceb0876056938e4c73aa2482ff71b
      </div>

      <!-- Editing Section -->
      <div v-if="isEditing" class="profile-edit">
        <div class="profile-edit-header">
          <div class="profile-picture-container">
            <label class="profile-upload">
              <input type="file" @change="handleFileUpload" hidden />
              <img :src="user.profilePicture || '/user.png'" alt="Profile Picture" class="profile-picture" />
            </label>
          </div>
          <input v-model="user.name" class="input-field" placeholder="Enter Name" />
          <input v-model="user.headline" class="input-field" placeholder="Enter Headline" />
        </div>

        <div class="profile-edit-section">
          <h3>About</h3>
          <textarea v-model="user.about" class="input-field" placeholder="Enter About"></textarea>
        </div>

        <div class="profile-edit-section">
          <h3>Experience</h3>
          <ul>
            <li v-for="(job, index) in user.experience" :key="index">
              <strong>{{ job.position }}</strong> at {{ job.company }} ({{ job.duration }})
              <button @click="deleteItem(user.experience, index)" class="btn btn-delete">Delete</button>
            </li>
          </ul>
          <input v-model="newExperience.position" class="input-field" placeholder="Position" />
          <input v-model="newExperience.company" class="input-field" placeholder="Company" />
          <input v-model="newExperience.duration" class="input-field" placeholder="Duration" />
          <button class="btn btn-secondary" @click="addExperience">Add Experience</button>
        </div>

        <div class="profile-edit-section">
          <h3>Education</h3>
          <ul>
            <li v-for="(edu, index) in user.education" :key="index">
              <strong>{{ edu.degree }}</strong> - {{ edu.institution }} ({{ edu.year }})
              <button @click="deleteItem(user.education, index)" class="btn btn-delete">Delete</button>
            </li>
          </ul>
          <input v-model="newEducation.degree" class="input-field" placeholder="Degree" />
          <input v-model="newEducation.institution" class="input-field" placeholder="Institution" />
          <input v-model="newEducation.year" class="input-field" placeholder="Year" />
          <button class="btn btn-secondary" @click="addEducation">Add Education</button>
        </div>

        <div class="profile-edit-section">
          <h3>Skills</h3>
          <ul>
            <li v-for="(skill, index) in user.skills" :key="index">
              <input type="checkbox" :checked="true" /> {{ skill }}
            </li>
          </ul>
          <input v-model="newSkill" class="input-field" placeholder="Enter Skill" />
          <button class="btn btn-secondary" @click="addSkill">Add Skill</button>
        </div>

        <div class="profile-edit-section">
          <h3>Social Links</h3>
          <input v-model="user.socialLinks.twitter" class="input-field" placeholder="Enter Twitter URL" />
          <input v-model="user.socialLinks.linkedin" class="input-field" placeholder="Enter LinkedIn URL" />
          <input v-model="user.socialLinks.github" class="input-field" placeholder="Enter GitHub URL" />
          <input v-model="user.socialLinks.website" class="input-field" placeholder="Enter Website URL" />
        </div>

        <div class="profile-actions">
          <button class="btn btn-success" @click="saveProfile">Save</button>
          <button class="btn btn-secondary" @click="isEditing = false">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  max-width: 900px;
  margin: 30px auto;
  padding: 30px;
  background: #fff;
  border-radius: 15px;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}

.profile-layout {
  display: flex;
  gap: 30px;
}

.profile-view,
.profile-edit {
  flex: 1;
}

.profile-header {
  text-align: center;
}

.profile-picture-container {
  display: inline-block;
}

.profile-upload {
  cursor: pointer;
  display: inline-block;
}

.profile-picture {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 3px solid #ddd;
  object-fit: cover;
}

.profile-sections {
  margin-top: 30px;
}

.profile-section h3 {
  font-size: 1.5em;
  margin-bottom: 10px;
}

.profile-section ul {
  list-style-type: none;
  padding: 0;
}

.profile-section ul li {
  margin-bottom: 5px;
}

.profile-section a {
  color: #0073b1;
  text-decoration: none;
}

.profile-section a:hover {
  text-decoration: underline;
}

.input-field {
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
}

.input-field:focus {
  outline: none;
  border-color: #0073b1;
}

.btn-primary, .btn-success, .btn-secondary, .btn-delete {
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
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
}

.btn-primary:hover, .btn-success:hover, .btn-secondary:hover, .btn-delete:hover {
  opacity: 0.8;
}

.profile-actions {
  text-align: center;
  margin-top: 20px;
}
</style>