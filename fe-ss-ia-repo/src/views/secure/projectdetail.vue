<template>
  <div class="project-detail-container">
    <button @click="$router.back()" class="btn-back">← Volver al buscador</button>

    <div v-if="project" class="detail-card">
      <header class="detail-header">
        <span class="tag">{{ project.ia_type }}</span>
        <h1>{{ project.title }}</h1>
        <p class="meta">Publicado en {{ project.year }} | Por <strong>{{ project.author }}</strong></p>
      </header>

      <section class="detail-content">
        <div class="content-block">
          <h3>Resumen del Proyecto</h3>
          <p>{{ project.description || 'Sin descripción disponible.' }}</p>
        </div>

        <div class="content-block">
          <h3>Metodología y Herramientas</h3>
          <ul>
            <li v-for="(tool, index) in project.tools" :key="index">{{ tool }}</li>
          </ul>
        </div>
      </section>

      <footer class="detail-footer">
        <div class="download-section">
          <h3>Documentación</h3>
          <button class="btn-download">Descargar Reporte (PDF)</button>
          <button class="btn-github">Ver Repositorio</button>
        </div>
      </footer>
    </div>

    <div v-else class="error-message">
      <p>No se encontró la información del proyecto.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectDetail',
  data() {
    return {
      // En una app real, aquí harías una petición API usando el ID de la URL
      project: null
    }
  },
  mounted() {
    this.fetchProjectDetails();
  },
  methods: {
    fetchProjectDetails() {
      // Simulamos la obtención de datos
      const id = this.$route.params.id;
      // Aquí podrías filtrar tu array de resultados o hacer un fetch
      this.project = {
        id: id,
        title: "Detección de Anomalías en Imágenes Médicas",
        author: "Ing. Roberto Sánchez",
        ia_type: "Computer Vision",
        year: 2023,
        description: "Este proyecto utiliza redes neuronales convolucionales (CNN) para identificar patrones irregulares en radiografías de tórax, optimizando el tiempo de diagnóstico preventivo en un 30%.",
        tools: ["Python", "TensorFlow", "OpenCV", "Keras"]
      };
    }
  }
}
</script>

<style scoped>
.project-detail-container { padding: 40px; max-width: 900px; margin: 0 auto; }
.btn-back { background: none; border: none; color: #666; cursor: pointer; margin-bottom: 20px; }
.detail-card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.tag { background: #e3f2fd; color: #0d6efd; padding: 5px 12px; border-radius: 20px; font-weight: bold; }
h1 { margin: 15px 0; color: #1a202c; }
.meta { color: #718096; border-bottom: 1px solid #edf2f7; padding-bottom: 20px; }
.content-block { margin: 25px 0; }
h3 { color: #2d3748; margin-bottom: 10px; }
.btn-download, .btn-github { margin-right: 10px; padding: 10px 20px; border-radius: 6px; cursor: pointer; border: none; }
.btn-download { background: #0d6efd; color: white; }
.btn-github { background: #2d3748; color: white; }
</style>