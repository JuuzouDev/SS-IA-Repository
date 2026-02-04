import axiosInstance from './axios';

/**
 * Función que conecta con el Blueprint de Auth en el Backend
 * @param {Object} userData - Contiene email y password
 * @returns {Promise} - Respuesta del servidor
 */

export const loginUser = async (userData) => {
    
    try {
        // Conexion con el Blueprint en Python -> auth.py
        const response = await axiosInstance.post('/auth/login', userData);
        
        // Respuesta exitosa del BE, retorno de datos a FE
        if(response.data.token){
            //Guardar Token para interceptor de Axios
            localStorage.setItem('authToken', response.data.token);
            //Guardado de datos no sensibles
            localStorage.setItem('username', response.data.user.username);
            localStorage.setItem('userRole', response.data.user.role);
        }
        return response.data;

    } catch (error) {
        // Captura de Error de BE y lanzamiento a FE
        const errorMessage = error.response?.data?.message || 'Error de conexión con el servidor';
        throw new Error(errorMessage);
    }
};