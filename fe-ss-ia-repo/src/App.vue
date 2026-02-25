<template>
  <v-app>
    <v-app-bar flat color="black" border="b">
      <v-container class="d-flex align-center">
        <v-btn variant="text" to="/" class="text-h6 font-weight-black">
          FESC-IA
        </v-btn>

        <div class="ml-4 d-none d-sm-flex">
          <v-btn variant="text" to="/buscador">Buscador</v-btn>
          <v-btn v-if="isLoggedIn" variant="text" to="/add-project">Subir Proyecto</v-btn>
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


      <v-menu
        v-if="$route.path !== '/login'"
        v-model="chatOpen"
        :close-on-content-click="false"
        location="top end"
        offset="15"
        transition="slide-y-reverse-transition"
      >
        <template v-slot:activator="{ props }">
          <v-avatar
            v-bind="props"
            size="70"
            class="elevation-8 shadow-hover"
            position="fixed"
            style="bottom: 24px !important; right: 24px !important; z-index: 9999 !important; cursor: pointer; border: 2px solid #1976D2; background-color: white;"
          >
            <v-img
              :src="asistenteImg"
              alt="Asistente Virtual"
              cover
            >
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular indeterminate color="primary"></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-avatar>
        </template>

        <v-card width="320" height="420" elevation="12" class="d-flex flex-column rounded-lg">
          <v-toolbar color="primary" density="compact">
            <v-icon start class="ml-2">mdi-robot</v-icon>
            <v-toolbar-title class="text-body-1 font-weight-bold">Asistente FESC-IA</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon="mdi-close" variant="text" @click="chatOpen = false"></v-btn>
          </v-toolbar>
          
          <v-card-text class="flex-grow-1 overflow-y-auto pa-4 bg-grey-lighten-4">
            <div v-for="(msg, i) in mensajes" :key="i" 
                 :class="msg.sender === 'ia' ? 'd-flex justify-start' : 'd-flex justify-end'" 
                 class="mb-3">
              <v-sheet
                :color="msg.sender === 'ia' ? 'white' : 'primary'"
                :class="msg.sender === 'ia' ? 'text-black' : 'text-white'"
                class="pa-2 px-3 rounded-xl shadow-sm text-body-2"
                max-width="85%"
              >
                {{ msg.text }}
              </v-sheet>
            </div>
          </v-card-text>

          <v-divider></v-divider>
          
          <v-card-actions class="pa-2 bg-white">
            <v-text-field
              v-model="nuevoMensaje"
              placeholder="Escribe tu duda..."
              hide-details
              density="compact"
              variant="outlined"
              append-inner-icon="mdi-send"
              :loading="isWaitingIA"
              :disabled="isWaitingIA"
              @click:append-inner="enviarMensaje"
              @keyup.enter="enviarMensaje"
            ></v-text-field>
          </v-card-actions>
        </v-card>
      </v-menu>
    </v-main>
  </v-app>
</template>

<script>
// IMPORTACIÓN DE LA IMAGEN PARA WEBPACK
import asistenteImg from '@/assets/Asistente.jpg';
import { askAssistant } from './services/assistant_conect';


export default {
  name: 'App',
  data() {
    return {
      // VARIABLES DE SESIÓN
      token: localStorage.getItem('authToken'),
      username: localStorage.getItem('username'),
      
      // VARIABLES DEL ASISTENTE
      asistenteImg, // Pasamos la imagen al data
      chatOpen: false,
      nuevoMensaje: '',
      mensajes: [
        { text: '¡Hola! Soy el asistente del Repositorio FESC. ¿En qué puedo ayudarte?', sender: 'ia' }
      ],
      isWaitingIA: false,
    }
  },
  computed: {
    isLoggedIn() {
      return !!this.token;
    }
  },
  watch: {
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
      this.token = null;
      this.$router.push('/inicio');
    },
    async enviarMensaje(){
      if (!this.nuevoMensaje.trim()) return;
      const userText = this.nuevoMensaje;

      // 1.- Añadir mensaje de usuario a la lista
      this.mensajes.push({text: userText, sender: 'usuario'});
      this.nuevoMensaje = '';
      
      //2.- Añadir Mensaje de "Escribiendo"
      const loadintMsgIndex = this.mensajes.length;
      this.mensajes.push ({text: "Pensando...", sender: 'ia', isLoading: true});

      //Comunicacion con BE
      try{
        //3.- Llamada real al API
        const response =  await askAssistant(userText);

        //4.- Reemplazar "Pensando" con la respuesta real
        this.mensajes[loadintMsgIndex].text = response;
        this.mensajes[loadintMsgIndex].isLoading = false;
      
      } catch (error) { 
        //Manejo de error visual
        this.mensajes[loadintMsgIndex].text = 'Lo siento, tuve un error al conectarme con mi motor de IA. Intentalo de nuevo mas tarde.';
        this.mensajes[loadintMsgIndex].isLoading = false;
      }

    }

  }
}
</script>

<style>
.background-full {
    background-color: white !important; 
}

.full-height-main {
    min-height: 100vh !important;
    width: 100vw !important;
}

.shadow-hover:hover {
  transform: scale(1.05);
  transition: transform 0.2s;
}

/* Forzar que el avatar se mantenga sobre todo el contenido del buscador */
.v-avatar {
  position: fixed !important;
}
</style>