<template>
  <v-container v-if="!loading && project">
    <v-card class="pa-6">
      <v-card-title class="text-h4">{{ project.title }}</v-card-title>
      <v-divider class="my-4"></v-divider>
      
      <v-row>
        <v-col cols="12" md="8">
          <h3>Resumen</h3>
          <p>{{ project.summary }}</p>
          
          <h3 class="mt-4">Metodología</h3>
          <p>{{ project.methodology }}</p>
        </v-col>
        
        <v-col cols="12" md="4" class="bg-grey-lighten-4 pa-4 rounded">
          <p><strong>Autores:</strong> {{ project.authors }}</p>
          <p><strong>Año:</strong> {{ project.year }}</p>
          <p><strong>Tipo de IA:</strong> {{ project.ai_type }}</p>
          
          <v-btn 
            block color="primary" class="mt-4"
            :href="`http://localhost:5000/static/uploads/reports/${project.pdf_path}`"
            target="_blank"
          >
            Descargar PDF
          </v-btn>
          
          <v-btn 
            v-if="project.repository_url"
            block variant="outlined" class="mt-2"
            :href="project.repository_url" target="_blank"
          >
            Ver Repositorio
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
  
  <v-container v-else-if="loading" class="text-center">
    <v-progress-circular indeterminate color="primary"></v-progress-circular>
  </v-container>
</template>

<script>
import { getProjectByID } from '@/services/projects-conect';

export default {
  name: 'ProjectDetail',
  data(){
    return {
      project: null,
      loading : true,
      error: null,
    }
  },
  async mounted(){
    const id =  this.$route.params.id; //Obtener id de la url
    try { 
      const response = await getProjectByID(id);
      if (response.status === 'success'){
        this.project = response.data;
      }
    } catch (err) { 
      this.error =  "No se pudo cargar la informacion del proyecto.";
    } finally { 
      this.loading = false;
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