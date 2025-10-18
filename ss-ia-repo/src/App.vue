<template>
  <router-view>
  </router-view>
  
</template>
<script>
export default {
  // AJUSTE CLAVE: El nombre del componente coincide con tu archivo
  name: 'App'
}
</script>

<style scoped>
/* Contenedor principal sin padding para que la sección hero ocupe el ancho */



/* Media query para mejorar la experiencia en pantallas pequeñas */
@media (max-width: 600px) {
    .cta-buttons {
        flex-direction: column;
    }
    .btn {
        width: 100%; /* Botones de ancho completo en móvil */
    }
}
</style>
