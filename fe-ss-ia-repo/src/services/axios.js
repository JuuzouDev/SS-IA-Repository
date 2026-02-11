import axios from 'axios';

const axiosInstance = axios.create({
    // Direccionando a la raiz del proyecto en flask
    baseURL: 'http://localhost:5000', 
    timeout: 10000,
});

// Interceptor para el token (se mantiene general)
axiosInstance.interceptors.request.use((config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    Promise.reject(error)
});

export default axiosInstance;