import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import SigninView from '../views/SigninView.vue'
import Dashboard from '../views/DashboardView.vue'
import Course from '../views/CourseView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/registroestudiante',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/iniciosesion',
      name: 'signin',
      component: SigninView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/cursos',
      name: 'cursos',
      component: Course
    }
  ]
})

export default router;
