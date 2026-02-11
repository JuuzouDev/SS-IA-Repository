<template>
  <v-container fluid class="pa-0 fill-height full-screen-fix"> 
    
    <v-sheet
      class="hero-section text-left fill-height"
      color="transparent"  
      min-height="100vh" 
      elevation="0" 
    >
      <v-container fluid class="pa-0 fill-height d-flex justify-center align-center"> 
        
        <div 
          class="transparent-blue-box text-center" 
          style="background-color: rgba(240, 248, 255, 0.9); max-width: 900px; padding: 40px;"
        >
            
            <h1 
              class="text-h3 text-sm-h2 mb-2 font-weight-black" 
              style="color: #333333; line-height: 1.1;" 
            >
              Repositorio Digital
              <br>
              FESC
            </h1>
            
            <h2 class="text-h5 text-sm-h4 mb-6 font-weight-medium" style="color: #555555;">
              Inteligencia Artificial & Servicio Social
            </h2>
            
            <p class="text-subtitle-1 mb-8" style="color: #777777;">
              Explora y gestiona proyectos de vanguardia en Inteligencia Artificial y reportes de Servicio Social de la comunidad FESC. Conecta el conocimiento académico con la solución de problemas reales.
            </p>

            

            <div class="cta-buttons d-flex flex-wrap justify-center" style="gap: 20px;"> 
              
              <v-btn 
                large 
                color="primary" 
                class="px-6 font-weight-medium" 
                to="/buscador"
                elevation="0"
                
              >
                <v-icon left>mdi-magnify</v-icon> Explorar Proyectos
              </v-btn>
              
              <v-btn 
                large 
                color="primary" 
                class="px-6 font-weight-medium" 
                to="/asistente"
                elevation="0"
              >
                <v-icon left>mdi-magnify</v-icon>Preguntar a GEMINI
              </v-btn>
            </div>
        </div>
        
      </v-container>
    </v-sheet>

  </v-container>
</template>

<script>
// La importación de la imagen del robot es necesaria si usas la imagen de fondo en el CSS
import robotImage from '@/assets/fondo2.png'; 

export default{
  name: 'home_main_centered_full_screen_bg_fixed',
  data() {
    return {
      robotImage: robotImage
    };
  },
}
</script>

<style scoped>
/*ANULACIÓN DE DIMENSIONES PARA CUBRIR TODA LA PANTALLA (Fix de 100vw/100vh) */
.full-screen-fix {
    width: 100vw !important;
    max-width: 100vw !important;
    height: 100vh !important;
    margin: 0 !important; 
    padding: 0 !important;
}

/*Estilos para la imagen de fondo en el v-sheet */
.hero-section {
    position: relative; /* Asegura que el contenido esté apilado correctamente */
    display: flex;
    align-items: center; 
    padding: 0; 
    width: 100%; 
    height: 100%;
    
    /* Aplicación de la imagen */
    background-image: url('~@/assets/fondo2.png'); 
    background-size: cover;      /* Escala la imagen para cubrir todo el contenedor */
    background-position: center; /* Centra la imagen */
    background-repeat: no-repeat;
}

/* Estilo para el recuadro flotante */
.transparent-blue-box {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05); /* Sombra ligera */
    border-radius: 8px;
    z-index: 1; 
}

.v-container.fluid.pa-0 {
    overflow: hidden; 
}
</style>