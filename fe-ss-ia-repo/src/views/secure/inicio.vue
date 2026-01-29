<template>
  
  <v-container fluid class="pa-0"> 
    
    <v-sheet
      class="hero-section text-left"
      color="#F0F8FF" 
      min-height="450"
      elevation="0" 
    >
      <v-container class="py-10 px-6"> 
        
        <v-row>
          
          <v-col cols="12" md="7">
            
            <h1 
              class="text-h4 text-sm-h3 mb-2 font-weight-black" 
              style="color: #333333; line-height: 1.1; white-space: nowrap;"
            >
              Repositorio Digital - FESC
            </h1>
            
            <h2 class="text-h5 text-sm-h4 mb-6 font-weight-medium" style="color: #555555;">
              Inteligencia Artificial & Servicio Social
            </h2>
            
            <p class="text-subtitle-1 mb-8" style="max-width: 500px; color: #777777;">
              Explora y gestiona proyectos de vanguardia en Inteligencia Artificial y reportes de Servicio Social de la comunidad FESC. Conecta el conocimiento académico con la solución de problemas reales.
            </p>

            <v-divider style="max-width: 50px;" class="mb-8"></v-divider>

            <div class="cta-buttons d-flex flex-wrap align-center" style="gap: 15px;">
              
              <v-btn 
                large 
                depressed
                color="primary" 
                class="white--text font-weight-bold" 
                style="width: 280px; height: 50px;"
                to="/buscador"
              >
                <v-icon left color="white">mdi-magnify</v-icon> EXPLORAR REPOSITORIO
              </v-btn>
              
              <v-btn 
                large 
                depressed
                color="primary" 
                class="white--text font-weight-bold" 
                style="width: 280px; height: 50px;"
                to="/asistente"

              >
                <v-icon left color="white">mdi-robot-outline</v-icon>
                PREGUNTALE A GEMINI
              </v-btn>
            </div>
            
          </v-col>
          
          <v-col cols="12" md="5" class="d-none d-md-flex justify-center align-center">
            <v-img
              :src="robotImage"  alt="Interacción humano-robot e IA"
              contain 
              max-height="400px" 
            ></v-img>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>

  </v-container>
</template>

<script>
// ¡IMPORTACIÓN CLAVE! Esto asegura que Webpack procese correctamente la imagen.
import robotImage from '@/assets/image_268ab0.jpg'; 

export default{
  name: 'home_main_with_image_fix',
  data() {
    return {
      // Hacemos la imagen accesible en el template a través de esta propiedad
      robotImage: robotImage 
    };
  },
}
</script>

<style scoped>
.hero-section {
  display: flex;
  align-items: center; 
}
</style>