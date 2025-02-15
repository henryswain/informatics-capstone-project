<script setup>
import { ref } from 'vue';

const user = ref({
  name: "Input Name",
  email: "Input Email",
  bio: "Input Bio",
  location: "Location",
  profilePicture: "/user.png",
});

const isEditing = ref(false);

const saveProfile = () => {
  isEditing.value = false;
  console.log("Profile updated:", user.value);
};
</script>

<template>
  <div class="profile-container">
    <div class="profile-header">
      <img :src="user.profilePicture" alt="Profile Picture" class="profile-picture" />
      
      <template v-if="isEditing">
        <input v-model="user.name" class="input-field" placeholder="Enter Name" />
      </template>
      <template v-else>
        <h2>{{ user.name }}</h2>
      </template>
      
      <p class="email">
        <template v-if="isEditing">
          <input v-model="user.email" class="input-field" placeholder="Enter Email" />
        </template>
        <template v-else>
          {{ user.email }}
        </template>
      </p>

      <p class="bio">
        <template v-if="isEditing">
          <textarea v-model="user.bio" class="input-field" placeholder="Enter Bio"></textarea>
        </template>
        <template v-else>
          {{ user.bio }}
        </template>
      </p>

      <p class="location">
        <template v-if="isEditing">
          <input v-model="user.location" class="input-field" placeholder="Enter Location" />
        </template>
        <template v-else>
          {{ user.location }}
        </template>
      </p>
    </div>

    <div class="profile-actions">
      <button v-if="!isEditing" class="btn btn-primary" @click="isEditing = true">Edit Profile</button>
      <button v-else class="btn btn-success" @click="saveProfile">Save</button>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  text-align: center;
  background: #ffffff;
  border-radius: 10px;
}

.profile-header {
  background: #b4b4b4;
  padding: 20px;
  border-radius: 10px;
}

.profile-picture {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 3px solid #d8d8d8;
}

.input-field {
  width: 80%;
  padding: 8px;
  margin: 5px 0;
  border: 1px solid #ccc;
  background: #ffffff;
}

.profile-actions {
  margin-top: 15px;
}

.btn {
  padding: 10px 15px;
  font-size: 14px;
  cursor: pointer;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-success {
  background-color: #28a745;
  color: white;
}
</style>