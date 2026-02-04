import axiosInstance from './axios';

const PREFIX = '/projects';

const ProjectService = {
    async uploadProject(formData) {
        // La URL final será: /api/projects/upload
        // axiosInstance ya detecta si es FormData gracias a lo que configuramos antes
        const response = await axiosInstance.post(`${PREFIX}/upload`, formData);
        return response.data;
    },
    
    async getAll() {
        // La URL final será: /api/projects/list
        const response = await axiosInstance.get(`${PREFIX}/list`);
        return response.data;
    }
};

export default ProjectService;