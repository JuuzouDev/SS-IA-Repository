import { createRouter, createWebHistory } from 'vue-router';
const routes = [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/inicio',
    name: 'inicio',
    component: () => import('@/views/secure/home_main.vue'), 
    meta: { requiresAuth: false }, // Meta definido correctamente
},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


// Protección de rutas
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('authToken'); // Verifica si hay un token
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/'); // Redirige al login si no está autenticado
  } else {
    next(); // Permite el acceso
  }
});

export default router;