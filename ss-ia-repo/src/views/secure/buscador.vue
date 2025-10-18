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
          <select id="ia-filter" v-model="filterIA" @change="performSearch(true)">
            <option value="">Mostrar todos</option>
            <option value="Deep Learning">Deep Learning</option>
            <option value="Computer Vision">Visión Artificial</option>
            <option value="NLP">Procesamiento de Lenguaje Natural (NLP)</option>
            <option value="Generativa">IA Generativa</option>
          </select>
        </div>

        <div class="filter-group">
          <label for="year-filter">Año de Publicación</label>
          <input type="number" id="year-filter" v-model="filterYear" @keyup.enter="performSearch(true)" placeholder="Ej. 2024">
        </div>

        </aside>

      <main class="results-area">
        
        <div class="search-controls">
          <input 
            type="text" 
            v-model="searchTerm" 
            @keyup.enter="performSearch()" 
            placeholder="Buscar por título, autor o palabra clave..."
            aria-label="Campo de búsqueda de proyectos"
          />
          <button @click="performSearch()" :disabled="isLoading" class="btn-search">
            {{ isLoading ? 'Buscando...' : 'Buscar' }}
          </button>
        </div>

        <div v-if="results.length >= 0" class="results-list">
          <h2>Resultados encontrados ({{ results.length }})</h2>
          
          <div v-for="project in results" :key="project.id" class="project-card" role="article">
            <h3>{{ project.title }}</h3>
            <p><strong>Autor(es):</strong> {{ project.author }}</p>
            <p><strong>Tipo de IA:</strong> <span class="tag">{{ project.ia_type }}</span></p>
            <p><strong>Año:</strong> {{ project.year }}</p>
            
            <router-link :to="{ name: 'project-detail', params: { id: project.id } }" class="details-link">
              Ver resumen completo →
            </router-link>
          </div>
        </div>

        <p v-else-if="!isLoading && searchPerformed" class="no-results">
          No se encontraron proyectos que coincidan con tus criterios. Intenta con otras palabras clave.
        </p>
        <p v-else-if="error" class="error-message">
          Ocurrió un error al buscar: {{ error }}
        </p>
        <p v-else class="initial-message">
          Usa la barra de búsqueda o los filtros laterales para empezar a explorar.
        </p>
      </main>

    </div>
  </div>
</template>

<script>
export default {
  name: 'fescia_buscador'
}

</script>