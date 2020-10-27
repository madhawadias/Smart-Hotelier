import React, { Component } from 'react'
import './Report.scss'

import SentimentAnalysisChart from './components/SentimentAnalysisChart/SentimentAnalysisChart'
import AspectRadarChart from './components/AspectRadarChart/AspectRadarChart'
import WordCloud from './components/WordCloud/WordCloud'
import { Paper } from '@material-ui/core'

export default class report extends Component<{ theme: string }> {

    render() {
        return (
            <div>
                <Paper className='head'>
                    The Kingsbury Colombo,Sri Lanka  vs  Hotel The Galadari, Colombo, Sri Lanka
                </Paper>
                <div className='row-2'>
                    <div className='item'>
                        <SentimentAnalysisChart theme={this.props.theme} />
                    </div>
                    <div className='item'>
                        <AspectRadarChart theme={this.props.theme} />
                    </div>
                </div>
                <div className='row-2'>
                    <div className='item'>
                        <WordCloud/>
                    </div>
                </div>

            </div>
        )
    }
}
