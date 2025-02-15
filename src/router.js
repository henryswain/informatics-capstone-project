
import { createRouter, createWebHistory } from 'vue-router';
import FindJobs from './pages/FindJobs.vue'; 
import ProfilePage from './pages/ProfilePage.vue';

// eventually will add imports like a PostJob that link to './pages.Postjob.vue'
// Will also add one for companies and career advice. But we will talk more about that 

const routes = [
  {
    path: '/',
    redirect: '/find-jobs' 
  },
  {
    path: '/find-jobs',
    name: 'FindJobs',
    component: FindJobs,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfilePage,
  }
  // we can add our future routes here for the post job and comapnies
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
