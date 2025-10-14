<template>
  <div class="home-container">
    
    <section class="hero-section">
      <h1>Repositorio Digital de la FESC: Inteligencia Artificial y Servicio Social</h1>
      
      <p class="subtitle">
        Explora y gestiona proyectos innovadores. Conecta el conocimiento académico con soluciones reales de IA y compromiso social.
      </p>

      <div class="cta-buttons">
        <router-link to="/buscador" class="btn btn-primary">
          Explorar Proyectos Ahora
        </router-link>
        
        <router-link to="/asistente" class="btn btn-secondary">
          Preguntar al Asistente GPT-5
        </router-link>
      </div>
    </section>

    </div>
</template>
<script>
export default {
  // AJUSTE CLAVE: El nombre del componente coincide con tu archivo
  name: 'InicioView' 
}
</script>

<style scoped>
/* Contenedor principal sin padding para que la sección hero ocupe el ancho */
.home-container {
  padding: 0; 
  text-align: center;
}

/* ---------------- HERO SECTION ---------------- */
.hero-section {
  background-color: #f0f4f8; 
  color: #1a2a40; 
  padding: 80px 20px; 
  border-radius: 0 0 15px 15px;
}

.hero-section h1 {
  font-size: clamp(2rem, 5vw, 2.8rem); 
  margin-bottom: 15px;
  line-height: 1.2;
}

.subtitle {
  font-size: clamp(1rem, 2.5vw, 1.3rem);
  color: #555;
  margin-bottom: 40px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

/* ---------------- BOTONES CTA  ---------------- */
.cta-buttons {
  margin-top: 30px;
  display: flex;
  flex-wrap: wrap; 
  justify-content: center;
  gap: 20px; 
}

.btn {
  padding: 15px 30px;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  text-decoration: none; 
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
}

.btn-primary {
  background-color: #007bff; /* Azul profesional */
  color: white;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-secondary {
  background-color: #42b983; /* Verde Vue, color de tecnología */
  color: white;
}

.btn-secondary:hover {
  background-color: #35a473;
}

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
