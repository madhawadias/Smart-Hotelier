import { Paper } from '@material-ui/core'
import React, { Component } from 'react'
import './WordCloud.scss'
import ReactWordcloud from 'react-wordcloud'
import ReportApi from '../../../../core/report-api'

export interface SentimentObject {
    name?: string;
    type?: string;
    data?: Array<number>;
    wordcloud: Array<object>
}

export default class WordCloud extends Component {
    state={
        words:[]

    }

    componentDidMount() {
        this.getSentimentReport()

    }

    async getSentimentReport() {
        let sentimentReport: SentimentObject[] = []

        try {
            sentimentReport = await ReportApi.getSentimentReport()
        } catch (err) {
            console.log("wordcloud report api error")
        }

        // for (let i = 0; i < sentimentReport.length; i++) {

        //     let singleObject = {
        //         name: sentimentReport[i].name,
        //         type: 'column',
        //         data: sentimentReport[i].data
        //     }

        //     newSentimentReport.push(singleObject)
        // }
        this.setState({
            words: sentimentReport[0].wordcloud
        })

    }
    
    render() {
        const {words} =this.state
        return (
            <div className='contain'>
                <Paper className='chart-section'>
                    <div className='title'>
                        Word Cloud Visualization
                    </div>
                    <ReactWordcloud
                        words={words}
                    />
                </Paper>
            </div>
        )
    }
}
