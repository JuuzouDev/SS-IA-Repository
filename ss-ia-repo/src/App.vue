<template>
  <v-app class="app-full-size"> <v-main class="background-full full-height-main"> 
      <router-view />
    </v-main>
  </v-app>
</template>

<style>
/* ... otros estilos ... */

.app-full-size {
    /* Anular el padding/margen que Vuetify aplica a veces al v-app o v-main */
    padding-top: 0 !important;
    margin-top: 0 !important;
}

.background-full {
    background-color: white !important; 
}

.full-height-main {
    /* Asegurar 100% de la altura de la ventana */
    min-height: 100vh !important;
    
    /* 🔑 CLAVE ADICIONAL: Asegurar que el ancho también sea 100% si hay limitación */
    width: 100vw !important;
}
</style>