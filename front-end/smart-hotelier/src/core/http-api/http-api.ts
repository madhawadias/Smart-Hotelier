import axios from 'axios';

export default class HttpApi {
    private host = 'http://localhost:2020/api';
    private token: string = '';

    setToken(token: string) {
        axios.defaults.headers.common['authorization'] = token;
    }

    async sendGetRequest(url: string) {
        const res = await axios.get(`${this.host}${url}`);
        const { success } = res.data;

        if (success) {
            return res.data;
        } else {
            const { errMessage } = res.data;
            throw new Error(errMessage);
        }
    }

    async sendPostRequest(url: string, data: any) {
        const res = await axios.post(`${this.host}${url}`, data);
        const { success } = res.data;

        if (success) {
            return res.data;
        } else {
            const { errMessage } = res.data;
            throw new Error(errMessage);
        }
    }

    async sendDeleteRequest(url: string) {
        const res = await axios.delete(`${this.host}${url}`);
        const { success } = res.data;

        if (success) {
            return res.data;
        } else {
            const { errMessage } = res.data;
            throw new Error(errMessage);
        }
    }
}