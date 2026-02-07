import axiosInstance from './axios';

/**
 * OBTENER PROYECTOS REGISTRADOS EN LA BD
 */
export const getAllProjects = async () => { 
    try{
        const response = await axiosInstance.get('/projects/load_projects');

        //Respuesta
        if(response.data.status === 'success'){
            return response.data.data;
        }
        return[];

    } catch (error) { 
        const errorMessage = error.response?.data?.message;
        throw new Error(errorMessage);
    }
}
/**
 * Obtener un solo proyecto
 */
export const getProjectByID = async (id) => {
    const response = await axiosInstance.get(`/projects/${id}`);
    return response.data; //Retorno del diccionario obtenido en Flask
}

/**
 * Subir un nuevo proyecto
 * Uso de FormData para que Axios configure el 'Content-Type: Multipart/form-data'.
 * *@param { FormData } projectFormData
 */
export const saveProject = async (projectFormData) => {
    /*console.log("=== RECIBIDO EN SERVICIO projects-conect.js ===");
    console.table(Object.fromEntries(projectFormData));
    */
   
    try {
        // Asegúrate de que axiosInstance tenga la BaseURL configurada
        console.log("Enviando a:", axiosInstance.defaults.baseURL + '/projects/upload');
        const response = await axiosInstance.post('/projects/upload', projectFormData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error detallado:", error.response); // Esto te dirá qué pasó
        const errorMessage = error.response?.data?.message || "Error de conexión con el servidor";
        throw new Error(errorMessage);
    }
};