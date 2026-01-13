<template>
  <v-container
    fluid
    class="login-background fill-height"
  >
    <v-row
      align="center"
      justify="center"
      class="fill-height"
      
    >
      <v-col cols="12" sm="8" md="5" lg="4">
        <v-card elevation="8" max-width="450" class="pa-6" style="margin-left: 60px;">
          
          <v-card-title class="text-h4 font-weight-black mb-2">
            ¿Olvidaste tu
          </v-card-title>
          <v-card-title class="text-h4 font-weight-black mb-2">
            contraseña?
          </v-card-title>

          <v-card-subtitle class="text-body-1 mb-6">
            Ingresa tu correo registrado
          </v-card-subtitle>

          <v-form @submit.prevent="handleLogin">
            <v-text-field
              label="Correo electrónico"
              v-model="email"
              variant="outlined"
              prepend-inner-icon="mdi-email-outline"
              placeholder="ejemplo@fesc.mx"
              class="mb-3"
            />


            <v-btn
              block
              color="primary"
              size="x-large"
              type="submit"
              class="font-weight-bold"
            >
              Enviar
            </v-btn>
          </v-form>

          <div class="d-flex flex-column align-start mt-6">
            <router-link to="/login" class="custom-link mb-3">
              Inicia Sesion
            </router-link>

            
          </div>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
export default {
  name: 'LoginView',
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    handleLogin () {
      // lógica de login
    }
  }
}
</script>
<style scoped>
.login-background {
  background-image: url('@/assets/loginbackground.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>

