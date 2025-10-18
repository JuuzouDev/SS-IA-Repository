<template>
  <div class="login-container">
    <div class="login-box">
      <h2>Iniciar Sesión</h2>
      
      <form @submit.prevent="login">
        
        <div class="form-group">
          <label for="username">Usuario:</label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            required 
            placeholder="Introduce tu usuario"
          >
        </div>
        
        <div class="form-group">
          <label for="password">Contraseña:</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            required 
            placeholder="Introduce tu contraseña"
          >
        </div>
        
        <button type="submit" class="btn-login">
          Acceder
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'fescia_login',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // 1. Aquí se manejaría la lógica de autenticación (API call, etc.)
      console.log('Intentando iniciar sesión con:', this.username, this.password);
      
      // 2. Si las credenciales son válidas, podrías redirigir al inicio:
      // this.$router.push('/inicio');
      
      // Lógica de ejemplo: si ambos campos están llenos
      if (this.username && this.password) {
        alert('Inicio de sesión simulado exitoso!');
      } else {
        alert('Por favor, rellena ambos campos.');
      }
    }
  }
};
</script>

<style scoped>
/* ----------------------------------- */
/* 1. CENTRADO TOTAL DE LA PÁGINA */
/* ----------------------------------- */
.login-container {
  display: flex;
  justify-content: center; /* Centrado horizontal */
  align-items: center; /* Centrado vertical */
  min-height: 100vh; /* Ocupa el 100% de la altura de la vista */
  background-color: #f4f7f6; /* Fondo suave */
}

/* ----------------------------------- */
/* 2. CAJA DE LOGIN */
/* ----------------------------------- */
.login-box {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px; /* Ancho máximo estándar para formularios */
}

.login-box h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

/* ----------------------------------- */
/* 3. CAMPOS DE FORMULARIO */
/* ----------------------------------- */
.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
  color: #555;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box; /* Importante para que el padding no desborde el ancho */
  transition: border-color 0.3s;
}

.form-group input:focus {
  border-color: #007bff;
  outline: none;
}

/* ----------------------------------- */
/* 4. BOTÓN */
/* ----------------------------------- */
.btn-login {
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: background-color 0.3s;
  margin-top: 10px;
}

.btn-login:hover {
  background-color: #0056b3;
}
</style>