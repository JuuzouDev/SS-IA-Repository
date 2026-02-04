<template>
  <v-app>
    <v-app-bar flat color="black" border="b">
      <v-container class="d-flex align-center">
        <v-btn variant="text" to="/" class="text-h6 font-weight-black">
          FESC-IA
        </v-btn>

        <div class="ml-4 d-none d-sm-flex">
          <v-btn variant="text" to="/buscador">Buscador</v-btn>
          <v-btn variant="text" to="/asistente">Asistente</v-btn>
        </div>

        <v-spacer />

        <template v-if="!isLoggedIn">
          <v-btn color="primary" variant="flat" to="/login">
            Iniciar sesión
          </v-btn>
        </template>

        <template v-else>
          <v-menu open-on-hover>
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                variant="text"
                class="text-none font-weight-bold"
                prepend-icon="mdi-account-circle"
              >
                {{ username }}
              </v-btn>
            </template>

            <v-list class="mt-2" elevation="4">
              <v-list-item @click="handleLogout" color="error">
                <template v-slot:prepend>
                  <v-icon icon="mdi-logout"></v-icon>
                </template>
                <v-list-item-title>Cerrar sesión</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </template>
      </v-container>
    </v-app-bar>

    <v-main class="background-full full-height-main">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      
      token: localStorage.getItem('authToken'),
      username: localStorage.getItem('username')
    }
  },
  computed: {
    isLoggedIn() {
      // Se actualiza si el token cambia en el data
      return !!this.token;
    }
  },
  watch: {
    // Detectar cambios en la ruta para refrescar el estado del token
    // (Útil si no usas Pinia todavía)
    '$route'() {
      this.token = localStorage.getItem('authToken');
      this.username = localStorage.getItem('username');
    }
  },
  methods: {
    handleLogout() {
      localStorage.removeItem('authToken');
      localStorage.removeItem('username');
      localStorage.removeItem('userRole');
      this.token = null; // Forzamos actualización visual
      this.$router.push('/login');
    }
  }
}
</script>

<style>
/* Tus estilos se mantienen igual */
.background-full {
    background-color: white !important; 
}

.full-height-main {
    min-height: 100vh !important;
    width: 100vw !important;
}
</style>