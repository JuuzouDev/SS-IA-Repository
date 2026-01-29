<template>
  <v-container fluid class="fill-height bg-grey-lighten-4 pa-0">
    <v-row no-gutters class="fill-height">
      <v-col cols="12" class="d-flex flex-column fill-height">
        
        <v-toolbar color="white" border="b" flat>
          <v-avatar color="primary" size="40" class="ml-4">
            <v-icon color="white">mdi-robot-outline</v-icon>
          </v-avatar>
          <v-toolbar-title class="font-weight-bold">Asistente Virtual FESC-IA</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon="mdi-dots-vertical"></v-btn>
        </v-toolbar>

        <v-container class="flex-grow-1 overflow-y-auto pa-4" style="max-height: calc(100vh - 140px);">
          <div v-for="(message, index) in chatHistory" :key="index" 
               :class="['d-flex mb-4', message.role === 'user' ? 'justify-end' : 'justify-start']">
            
            <v-card
              :color="message.role === 'user' ? 'primary' : 'white'"
              :theme="message.role === 'user' ? 'dark' : 'light'"
              elevation="1"
              max-width="80%"
              :class="['pa-3', message.role === 'user' ? 'rounded-be-0' : 'rounded-bs-0']"
            >
              <div class="text-body-1">{{ message.content }}</div>
              <div class="text-caption mt-1 opacity-70 text-right">
                {{ message.time }}
              </div>
            </v-card>
          </div>

          <div v-if="isTyping" class="d-flex justify-start mb-4">
            <v-card color="white" elevation="1" class="pa-3 rounded-bs-0">
              <v-progress-circular indeterminate size="20" width="2" color="primary"></v-progress-circular>
              <span class="ml-2 text-caption">Gemini está procesando...</span>
            </v-card>
          </div>
        </v-container>

        <v-footer app color="white" border="t" class="pa-2">
          <v-container class="pa-0">
            <v-row no-gutters align="center">
              <v-col>
                <v-text-field
                  v-model="newMessage"
                  placeholder="Escribe tu consulta aquí..."
                  variant="solo-filled"
                  flat
                  hide-details
                  @keyup.enter="simulateReply"
                  rounded="lg"
                >
                  <template v-slot:append-inner>
                    <v-btn
                      icon="mdi-send"
                      variant="text"
                      color="primary"
                      :disabled="!newMessage.trim() || isTyping"
                      @click="simulateReply"
                    ></v-btn>
                  </template>
                </v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-footer>

      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';



const newMessage = ref('');
const isTyping = ref(false);

// Historial inicial
const chatHistory = ref([
  { 
    role: 'assistant', 
    content: '¡Hola! Soy el asistente inteligente de la FESC. Puedo ayudarte con dudas sobre el servicio social o búsqueda de proyectos de IA. ¿En qué puedo apoyarte?', 
    time: '10:00 AM' 
  }
]);

// Función temporal para simular la respuesta (Mockup)
const simulateReply = () => {
  if (!newMessage.value.trim()) return;

  const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  // 1. Agregar mensaje del usuario
  chatHistory.value.push({
    role: 'user',
    content: newMessage.value,
    time: currentTime
  });

  const userQuery = newMessage.value;
  newMessage.value = '';
  isTyping.value = true;

  // 2. Simular espera del servidor y respuesta
  setTimeout(() => {
    isTyping.value = false;
    chatHistory.value.push({
      role: 'assistant',
      content: `Esta es una respuesta simulada a: "${userQuery}". Muy pronto estaré conectado al motor de Gemini en el backend.`,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    });
  }, 1500);
};
</script>

<style scoped>
/* Estilo para que el contenedor de mensajes ocupe el espacio disponible */
.fill-height {
  height: 100vh;
}

/* Personalización de los bordes para estilo burbuja de chat */
.rounded-be-0 {
  border-bottom-right-radius: 0 !important;
}
.rounded-bs-0 {
  border-bottom-left-radius: 0 !important;
}
</style>