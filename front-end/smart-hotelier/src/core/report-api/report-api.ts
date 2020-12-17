import httpApi from '../http-api'

export default class ReportApi {

    async getSentimentReport(): Promise<[]>{
        let SentimentReport:[]  = await httpApi.sendGetRequest('/report/sentimentAnalyse')
        return SentimentReport;
    }

    async Report() {
        const SentimentReport = await httpApi.sendGetRequest('/report');
        return SentimentReport;
    }


    // async createProject(project: Project) {
    //     await httpApi.sendPostRequest('/project', project);
    // }

    // async getProjects(): Promise<Project[]> {
    //     const { projects } = await httpApi.sendGetRequest('/project');
    //     return projects;
    // }

    // async searchProjects(value: string): Promise<Project[]> {
    //     const { projects } = await httpApi.sendGetRequest(`/project/search/${value}`);
    //     return projects;
    // }

    // async deleteProject(id: string) {
    //     await httpApi.sendDeleteRequest(`/project/${id}`);
    // }

    // async getProjectById(id: string): Promise<Project> {
    //     const { project } = await httpApi.sendGetRequest(`/project/${id}`);
    //     return project;
    // }

    // async updateProject(id: string, updates: any) {
    //     await httpApi.sendPostRequest(`/project/${id}`, updates);
    // }
   
}
