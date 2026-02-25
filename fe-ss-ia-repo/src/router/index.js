import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    redirect: 'Inicio', // cambie logingView por inicio
   // component: () => import('@/views/secure/login.vue')
  },
  {
  path: '/inicio',
  name: 'inicio',
  component: () => import('@/views/secure/home_main.vue'),
  meta: { requiresAuth: false }
  },
  {
    path: '/buscador',
    name: 'buscador',
    component: () => import('@/views/secure/buscador.vue'),
    meta: { requiresAuth : false} 
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/secure/loginView.vue'),
    meta: { requiresAuth : false} 
  },
  {
    path: '/forgot-password',
    name: 'forgot-password',
    component: () => import('@/views/secure/forgotpw.vue'),
    meta: { requiresAuth : false}
  }, 
  {
    path: '/add-project',
    name: 'add-project',
    component: () => import('@/views/secure/Add-project.vue'),
    meta: { requiresAuth : false}
  }, 
  {
  path: '/proyecto/:id',
  name: 'ProjectDetail',
  component: () => import('@/views/secure/projectdetail.vue')
}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


// Protección de rutas
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('authToken'); // Verifica si hay un token
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login'); // Redirige al login si no está autenticado
  } else {
    next(); // Permite el acceso
  }
});

export default router;