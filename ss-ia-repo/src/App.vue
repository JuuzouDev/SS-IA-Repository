<template>
  <v-app>
    <!-- NAVBAR GLOBAL -->
    <v-app-bar 
      flat
      color="black"
      border="b"
    >
      <v-container class="d-flex align-center">
        <v-btn variant="text" to="/" class="text-h6 font-weight-black">
          FESC-IA
        </v-btn>

        <div class="ml-4 d-none d-sm-flex">
          <v-btn variant="text" to="/buscador">Buscador</v-btn>
          <v-btn variant="text" to="/asistente">Asistente</v-btn>
        </div>

        <v-spacer />

        <v-btn color="primary" variant="flat" to="/login">
          Iniciar sesión
        </v-btn>
      </v-container>
    </v-app-bar>

    <!-- CONTENIDO DE LAS VISTAS -->
    <v-main class="background-full full-height-main">
      <router-view />
    </v-main>

  </v-app>
</template>

<style>

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