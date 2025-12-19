<template>
  <div class="search-view-container">
    <h1>Buscador de Proyectos y Trabajos FESC</h1>
    <p class="description">
      Encuentra proyectos de IA, reportes de servicio social y documentos relevantes.
    </p>

    <div class="search-layout">
      
      <aside class="filters-panel">
        <h2>Filtros</h2>
        
        <div class="filter-group">
          <label for="ia-filter">Tipo de Inteligencia Artificial</label>
          <select id="ia-filter" v-model="filterIA" @change="performSearch">
            <option value="">Mostrar todos</option>
            <option value="Deep Learning">Deep Learning</option>
            <option value="Computer Vision">Visión Artificial</option>
            <option value="NLP">Procesamiento de Lenguaje Natural (NLP)</option>
            <option value="Generativa">IA Generativa</option>
          </select>
        </div>

        <div class="filter-group">
          <label for="year-filter">Año de Publicación</label>
          <input 
            type="number" 
            id="year-filter" 
            v-model="filterYear" 
            @keyup.enter="performSearch" 
            placeholder="Ej. 2024"
          >
        </div>
      </aside>

      <main class="results-area">
        
        <div class="search-controls">
          <input 
            type="text" 
            v-model="searchTerm" 
            @keyup.enter="performSearch" 
            placeholder="Buscar por título, autor o palabra clave..."
            aria-label="Campo de búsqueda de proyectos"
          />
          <button @click="performSearch" :disabled="isLoading" class="btn-search">
            {{ isLoading ? 'Buscando...' : 'Buscar' }}
          </button>
        </div>

        <div v-if="results && results.length > 0" class="results-list">
          <h2>Resultados encontrados ({{ results.length }})</h2>
          
          <div v-for="project in results" :key="project.id" class="project-card" role="article">
            <h3>{{ project.title }}</h3>
            <p><strong>Autor(es):</strong> {{ project.author }}</p>
            <p><strong>Tipo de IA:</strong> <span class="tag">{{ project.ia_type }}</span></p>
            <p><strong>Año:</strong> {{ project.year }}</p>
            
            <a href="#" class="details-link" @click.prevent>
              Ver resumen completo →
            </a>
          </div>
        </div>

        <p v-else-if="!isLoading && searchPerformed" class="no-results">
          No se encontraron proyectos.
        </p>
        <p v-else class="initial-message">
          Usa la barra de búsqueda o los filtros para explorar.
        </p>
      </main>

    </div>
  </div>
</template>

<script>
export default {
  name: 'fescia_buscador',
  data() {
    return {
      searchTerm: '',
      filterIA: '',
      filterYear: null,
      isLoading: false,
      searchPerformed: true, // Lo dejamos en true para que veas los datos de inmediato
      error: null,
      results: [
        {
          id: 1,
          title: "Detección de Anomalías en Imágenes Médicas",
          author: "Ing. Roberto Sánchez",
          ia_type: "Computer Vision",
          year: 2023
        },
        {
          id: 2,
          title: "Chatbot para Atención al Alumno FESC",
          author: "Alicia Villanueva",
          ia_type: "NLP",
          year: 2024
        },
        {
          id: 3,
          title: "Predicción de Tráfico mediante Redes Neuronales",
          author: "Carlos Méndez",
          ia_type: "Deep Learning",
          year: 2022
        }
      ]
    }
  },
  methods: {
    performSearch() {
      this.isLoading = true;
      setTimeout(() => {
        this.isLoading = false;
        this.searchPerformed = true;
      }, 500);
    }
  }
}
</script>

<style scoped>
.search-view-container { padding: 20px; color: #333; }
.search-layout { display: flex; gap: 20px; }
.filters-panel { width: 250px; background: #f8f9fa; padding: 15px; border-radius: 8px; }
.results-area { flex: 1; }
.search-controls { display: flex; gap: 10px; margin-bottom: 20px; }
.search-controls input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
.project-card { border: 1px solid #eee; padding: 15px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
.tag { background: #e3f2fd; color: #0d6efd; padding: 2px 8px; border-radius: 4px; font-size: 0.85em; }
.details-link { color: #0d6efd; text-decoration: none; font-weight: bold; }
.btn-search { background: #0d6efd; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
</style>