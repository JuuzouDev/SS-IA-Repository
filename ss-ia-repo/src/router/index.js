import { createRouter, createWebHistory } from 'vue-router';


const routes = [
  {
    path: '/',
    redirect: '/fescia/inicio',
  },
  {
    path: '/fescia',
    redirect: '/fescia/inicio',
  },
  {
    path: '/fescia/inicio',
    name: 'fescia_inicio',
    component: () => import('@/views/secure/inicio.vue'),
    meta: { requiresAuth : false }
  },
  {
    path: '/fescia/login',
    name: 'fescia_login',
    component: () => import('@/views/secure/login.vue'),
    meta: {requiresAuth: false }
  },
  {
    path: '/fescia/buscador',
    name: 'fescia_buscador',
    component: () => import('@/views/secure/buscador.vue'),
    meta: { requiresAuth : false} 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


/*// Protección de rutas
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('authToken'); // Verifica si hay un token
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/'); // Redirige al login si no está autenticado
  } else {
    next(); // Permite el acceso
  }
});*/

export default router;