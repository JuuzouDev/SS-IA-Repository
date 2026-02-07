<template>
  <v-container fluid class="pa-0 bg-grey-lighten-4" style="min-height: 100vh;">
    <v-sheet color="black" class="pa-10">
      <v-container>
        <h1 class="text-h4 font-weight-bold white--text">Registrar Nuevo Proyecto</h1>
        <p class="text-grey-lighten-1">Proporciona la información técnica y documentación del proyecto.</p>
      </v-container>
    </v-sheet>

    <v-container class="mt-n8">
      <v-row justify="center">
        <v-col cols="12" md="10" lg="8">
          <v-card elevation="2" class="pa-8" style="border-radius: 12px;">
            <v-form ref="formNode">
              
              <h3 class="text-subtitle-1 font-weight-bold mb-4 text-blue">INFORMACIÓN GENERAL</h3>
              
              <v-text-field
                v-model="form.titulo"
                label="Título del Proyecto"
                placeholder="Ej. Detección de Anomalías"
              ></v-text-field>

              <v-row>
                <v-col cols="12" sm="8">
                  <v-text-field v-model="form.autor" label="Autor(es)"></v-text-field>
                </v-col>
                <v-col cols="12" sm="4">
                  <v-text-field v-model="form.anio" label="Año" type="number"></v-text-field>
                </v-col>
              </v-row>

              <v-select
                v-model="form.tipo"
                :items="['Computer Vision', 'NLP', 'Machine Learning', 'Robótica']"
                label="Tipo de IA"
              ></v-select>

              <h3 class="text-subtitle-1 font-weight-bold mb-4 mt-4 text-blue">CONTENIDO Y METODOLOGÍA</h3>

              <v-textarea v-model="form.resumen" label="Resumen" auto-grow rows="3"></v-textarea>
              <v-text-field v-model="form.herramientas" label="Metodología"></v-text-field>

              <h3 class="text-subtitle-1 font-weight-bold mb-4 mt-4 text-blue">DOCUMENTACIÓN</h3>
              
              <v-row>
                <v-col cols="12" sm="6">
                  <v-text-field v-model="form.repoUrl" label="URL Repositorio" prepend-inner-icon="mdi-github"></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-file-input
                    label="Reporte (PDF)"
                    accept="application/pdf"
                    @update:modelValue="handleFileUpdate"
                  ></v-file-input>
                </v-col>
              </v-row>

              <v-divider class="my-6"></v-divider>

              <div class="d-flex justify-end" style="gap: 15px;">
                <v-btn variant="text" @click="$router.push('/buscador')">Cancelar</v-btn>
                <v-btn
                  color="primary"
                  size="large"
                  :loading="loading"
                  @click="handleSaveProject"
                >
                  GUARDAR PROYECTO
                </v-btn>
              </div>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-snackbar v-model="snackbar.show" :color="snackbar.color">
      {{ snackbar.text }}
    </v-snackbar>
  </v-container>
</template>



<script>
import { saveProject } from '@/services/projects-conect';

export default {
  name: 'AnadirProyecto',
  data() {
    return {
      loading: false,
      snackbar: { show: false, text: '', color: 'success' },
      form: {
        titulo: '',
        autor: '',
        anio: 2026,
        tipo: '',
        resumen: '',
        herramientas: '',
        repoUrl: '',
        pdfArchivo: null,
      },
    }
  },
  methods: {

    handleFileUpdate(file) {
      // Manejamos el archivo manualmente
      this.form.pdfArchivo = Array.isArray(file) ? file[0] : file;
    },

    async handleSaveProject() {
      // VALIDACIÓN MANUAL DE CAMPOS
      if (!this.form.titulo || !this.form.pdfArchivo) {
        this.showMsg("Título y PDF son obligatorios", "error");
        return;
      }

      this.loading = true;

      try {
        const formData = new FormData();
        formData.append('title', this.form.titulo);
        formData.append('authors', this.form.autor);
        formData.append('year', this.form.anio);
        formData.append('ai_type', this.form.tipo);
        formData.append('summary', this.form.resumen);
        formData.append('methodology', this.form.herramientas);
        formData.append('repository_url', this.form.repoUrl);
        formData.append('report', this.form.pdfArchivo);

        /**Verificacion de integridad del Form Data
        console.log("=== DATOS ENVIADOS DESDE VUE ===");
        for (let [key, value] of formData.entries()) {
          if (value instanceof File) {
            console.log(`${key}: [Archivo] ${value.name} (${value.size} bytes)`);
          } else {
            console.log(`${key}: ${value}`);
          }
        }
        */
        const response = await saveProject(formData);

        if (response.status === 'success') {
          this.showMsg("¡Proyecto guardado con éxito!", "success");
          setTimeout(() => this.$router.push('/buscador'), 1500);
        }

      } catch (e) {
        this.showMsg("Error en el servidor", "error");
      } finally {
        this.loading = false;
      }
    },
    showMsg(text, color = 'success') {
      this.snackbar.text = text;
      this.snackbar.color = color;
      this.snackbar.show = true;
    }
  }
}
</script>