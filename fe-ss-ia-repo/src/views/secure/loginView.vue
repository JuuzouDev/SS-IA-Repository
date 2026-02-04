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
            Iniciar Sesión
          </v-card-title>

          <v-card-subtitle class="text-body-1 mb-6">
            Ingresa tus credenciales para acceder.
          </v-card-subtitle>

          <!-- Formulario -->
          <v-form @submit.prevent="handleLogin">
            <v-text-field
              label="Usuario"
              v-model="usuario"
              variant="outlined"
              prepend-inner-icon="mdi-email-outline"
              placeholder="User"
              class="mb-3"
            />

            <v-text-field
              label="Contraseña"
              v-model="password"
              type="password"
              variant="outlined"
              prepend-inner-icon="mdi-lock-outline"
              class="mb-5"
            />

            <v-btn
              block
              color="primary"
              size="x-large"
              type="submit"
              class="font-weight-bold"
            >
              Entrar
            </v-btn>
          </v-form>

          <div class="d-flex flex-column align-start mt-6">
            <router-link to="/forgot-password" class="custom-link mb-3">
              ¿Olvidaste tu contraseña?
            </router-link>
          </div>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { loginUser } from '@/services/login-conect';

export default {
  name: 'LoginView',
  data () {
    return {
      usuario: '',   
      password: '',
    }
  },
  methods: {
    async handleLogin() {
      // 1. Validar que los campos no estén vacíos antes de disparar la lógica
      if (!this.usuario || !this.password) return;

      try {
        const response = await loginUser({
          user: this.usuario,
          password: this.password
        });
        
        if (response) {
          console.log('Login exitoso');
          // Usar el router de forma segura
          this.$router.push('/inicio');
        }
      } catch (error) {
        console.error('Error capturado:', error.message);
      }
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
