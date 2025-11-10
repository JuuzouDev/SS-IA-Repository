import axios from 'axios';

const axiosInstance = axios.create({
    baseUrl: 'http://localhost:5000/iaReposit',  //Link de conectividad con backend 
    timeout: 10000, //Tiempo de espera
    headers: {
        'Content-Type': 'application/json',
    }
});

// Interceptor de solicitud (para agregar token)
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);


// Interceptor de respuesta (para manejar errores globales)
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      console.warn('⚠️ Sesión expirada o no autorizada.');
      // Puedes redirigir al login aquí si lo deseas:
      // window.location.href = '/';
    }
    return Promise.reject(error);
  }
);

export default axiosInstance

