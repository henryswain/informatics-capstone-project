
import { createRouter, createWebHistory } from 'vue-router';
import FindJobs from './pages/FindJobs.vue'; 

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
  // we can add our future routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
