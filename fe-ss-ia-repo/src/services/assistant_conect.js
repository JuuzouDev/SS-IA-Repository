import axiosInstance from './axios';

export const askAssistant = async (message) => {
    try {
        const token = localStorage.getItem('authToken');

        const response = await axiosInstance.post('/assistant/ask', 
            {message: message},
        {
            headers:{
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            timeout: 30000 //Tiempo de espera de respuesta de 30 seg
        }
    );
    return response.data.answer; //Regresar solo texto de la respuesta

    } catch (error) {
        console.error("Error en la conexion con el asistente: ", error);
        throw error; 
    }
};