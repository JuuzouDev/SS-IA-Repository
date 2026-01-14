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
            v-model.number="filterYear" 
            @keyup.enter="performSearch" 
            placeholder="Ej. 2024"
          >
        </div>
        
        <button class="btn-clear" @click="clearFilters">Limpiar Filtros</button>
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

        <div v-if="filteredResults.length > 0" class="results-list">
          <h2>Resultados encontrados ({{ filteredResults.length }})</h2>
          
          <div v-for="project in filteredResults" :key="project.id" class="project-card" role="article">
            <h3>{{ project.title }}</h3>
            <p><strong>Autor(es):</strong> {{ project.author }}</p>
            <p><strong>Tipo de IA:</strong> <span class="tag">{{ project.ia_type }}</span></p>
            <p><strong>Año:</strong> {{ project.year }}</p>
            
            <router-link 
              :to="{ name: 'ProjectDetail', params: { id: project.id } }" 
              class="details-link"
            >
              Ver resumen completo →
            </router-link>
          </div>
        </div>

        <div v-else-if="!isLoading" class="no-results">
          <p>No se encontraron proyectos que coincidan con tu búsqueda.</p>
        </div>
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
      searchPerformed: false,
      // Base de datos local de ejemplo
      allProjects: [
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
      ],
      filteredResults: []
    }
  },
  mounted() {
    // Cargar todos los proyectos al inicio
    this.filteredResults = [...this.allProjects];
  },
  methods: {
    performSearch() {
      this.isLoading = true;
      
      // Simulamos un retraso de red
      setTimeout(() => {
        this.filteredResults = this.allProjects.filter(project => {
          const matchText = project.title.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
                            project.author.toLowerCase().includes(this.searchTerm.toLowerCase());
          const matchIA = this.filterIA === '' || project.ia_type === this.filterIA;
          const matchYear = !this.filterYear || project.year === this.filterYear;
          
          return matchText && matchIA && matchYear;
        });
        
        this.isLoading = false;
        this.searchPerformed = true;
      }, 400);
    },
    clearFilters() {
      this.searchTerm = '';
      this.filterIA = '';
      this.filterYear = null;
      this.filteredResults = [...this.allProjects];
    }
  }
}
</script>

<style scoped>
.search-view-container { padding: 20px; color: #333; max-width: 1200px; margin: 0 auto; }
.search-layout { display: flex; gap: 20px; margin-top: 30px; }
.filters-panel { width: 280px; background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px solid #e9ecef; height: fit-content; }
.filter-group { margin-bottom: 20px; }
.filter-group label { display: block; margin-bottom: 8px; font-weight: bold; font-size: 0.9em; }
.filter-group select, .filter-group input { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }

.results-area { flex: 1; }
.search-controls { display: flex; gap: 10px; margin-bottom: 25px; }
.search-controls input { flex: 1; padding: 12px; border: 1px solid #ced4da; border-radius: 6px; font-size: 1rem; }

.project-card { border: 1px solid #eee; padding: 20px; margin-bottom: 20px; border-radius: 10px; background: #fff; transition: transform 0.2s, box-shadow 0.2s; }
.project-card:hover { transform: translateY(-3px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.tag { background: #e3f2fd; color: #0d6efd; padding: 4px 10px; border-radius: 4px; font-size: 0.85em; font-weight: bold; }
.details-link { display: inline-block; margin-top: 15px; color: #0d6efd; text-decoration: none; font-weight: bold; }

.btn-search { background: #0d6efd; color: white; border: none; padding: 0 25px; border-radius: 6px; cursor: pointer; font-weight: bold; }
.btn-clear { width: 100%; background: none; border: 1px solid #dee2e6; color: #6c757d; padding: 8px; border-radius: 4px; cursor: pointer; margin-top: 10px; }
.btn-clear:hover { background: #e9ecef; }
</style>