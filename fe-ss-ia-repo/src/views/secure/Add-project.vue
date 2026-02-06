<template>
  <v-container fluid class="pa-0 gray lighten-4" style="min-height: 100vh;">
    <v-sheet color="black" dark class="pa-10">
      <v-container>
        <h1 class="text-h4 font-weight-bold">Registrar Nuevo Proyecto</h1>
        <p class="grey--text text--lighten-1">Proporciona la información técnica y documentación del proyecto.</p>
      </v-container>
    </v-sheet>

    <v-container class="mt-n8">
      <v-row justify="center">
        <v-col cols="12" md="10" lg="8">
          <v-card elevation="2" class="pa-8" style="border-radius: 12px;">
            <v-form ref="form" @submit.prevent="saveProject">
              
              <h3 class="text-subtitle-1 font-weight-bold mb-4 blue--text">INFORMACIÓN GENERAL</h3>
              
              <v-text-field
                v-model="form.titulo"
                label="Título del Proyecto"
                outlined
                dense
                placeholder="Ej. Detección de Anomalías en Imágenes Médicas"
                required
              ></v-text-field>

              <v-row>
                <v-col cols="12" sm="8">
                  <v-text-field
                    v-model="form.autor"
                    label="Autor(es)"
                    outlined
                    dense
                    placeholder="Ing. Roberto Sánchez"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="4">
                  <v-text-field
                    v-model="form.anio"
                    label="Año"
                    outlined
                    dense
                    type="number"
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-select
                v-model="form.tipo"
                :items="['Computer Vision', 'NLP', 'Machine Learning', 'Robótica']"
                label="Tipo de Inteligencia Artificial"
                outlined
                dense
              ></v-select>

              <h3 class="text-subtitle-1 font-weight-bold mb-4 mt-4 blue--text">CONTENIDO Y METODOLOGÍA</h3>

              <v-textarea
                v-model="form.resumen"
                label="Resumen del Proyecto"
                outlined
                auto-grow
                rows="3"
              ></v-textarea>

              <v-text-field
                v-model="form.herramientas"
                label="Metodología y Herramientas (Separa con comas)"
                outlined
                dense
                placeholder="Python, TensorFlow, OpenCV..."
              ></v-text-field>

              <h3 class="text-subtitle-1 font-weight-bold mb-4 mt-4 blue--text">DOCUMENTACIÓN</h3>
              
              <v-row align="center">
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="form.repoUrl"
                    label="URL del Repositorio"
                    outlined
                    dense
                    prepend-inner-icon="mdi-github"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-file-input
                    label="Reporte (PDF)"
                    outlined
                    dense
                    accept="application/pdf"
                    prepend-icon="mdi-file-pdf-box"
                  ></v-file-input>
                </v-col>
              </v-row>

              <v-divider class="my-6"></v-divider>

              <div class="d-flex justify-end" style="gap: 15px;">
                <v-btn text color="grey darken-1" @click="$router.push('/buscador')">
                  Cancelar
                </v-btn>
                <v-btn
                  color="primary"
                  large
                  class="white--text font-weight-bold"
                  type="submit"
                >
                  GUARDAR PROYECTO
                </v-btn>
              </div>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: 'AnadirProyecto',
  data: () => ({
    form: {
      titulo: '',
      autor: '',
      anio: 2026,
      tipo: '',
      resumen: '',
      herramientas: '',
      repoUrl: ''
    }
  }),
  methods: {
    saveProject() {
      console.log("Datos capturados:", this.form);
      alert("¡Proyecto guardado exitosamente!");
      this.$router.push('/buscador');
    }
  }
}
</script>