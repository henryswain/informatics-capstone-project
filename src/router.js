
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router';
import HomePage from './pages/HomePage.vue';
import FindJobs from './pages/FindJobs.vue'; 
import ProfilePage from './pages/ProfilePage.vue';
import SavedJobs from './pages/SavedJobs.vue';
import LoginPage from './pages/Login.vue';
import RegisterPage from './pages/Register.vue';
import Settings from './pages/Settings.vue';

// eventually will add imports like a PostJob that link to './pages.Postjob.vue'
// Will also add one for companies and career advice. But we will talk more about that 

const routes = [
  {
    path: '/home-page',
    redirect: '/find-jobs' 
  },
  {
    path: '/find-jobs',
    name: 'FindJobs',
    component: FindJobs,
    props: route => ({ query: route.query.q })
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfilePage,
  },
  {
    path: '/saved-jobs',
    name: 'SavedJobs',
    component: SavedJobs,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage,
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings,
  }
  // we can add our future routes here for the post job and comapnies
];

const router = createRouter({
  // history: createWebHashHistory("/informatics-capstone-project/"),
  history: createWebHistory(),
  routes,
});

export default router;
