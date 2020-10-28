import httpApi from '../http-api'

export default class ReportApi {

    async getSentimentReport(){
        const { SentimentReport } = await httpApi.sendGetRequest('/report/sentimentAnalyse');
        return SentimentReport;
    }
   
}
