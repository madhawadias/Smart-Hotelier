import React, { Component } from 'react'
import './SentimentAnalysisChart.scss'
import ReactApexChart from 'react-apexcharts'
import { Paper } from '@material-ui/core'


export default class SentimentAnalysisChart extends Component<{ theme: string }> {

    state = {
        series: [{
            name: 'Kingsbury',
            type: 'column',
            data: [20, 30, 50]
        }, {
            name: 'Galadari',
            type: 'column',
            data: [50, 10, 40]
        }],
        options: {
            theme: {
                mode: this.props.theme
            },
            colors: ['#00667C', '#7B178B'],
            chart: {
                height: 350,
                width: 600,
                type: 'bar',
                stacked: false
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '50%',
                },
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            yaxis: {
                min: 0,
                max: 100,
                labels: {
                    show: true,
                    style: {
                        fontSize: '12px',
                        fontFamily: 'Roboto',
                        fontWeight: 400,
                        cssClass: 'apexcharts-xaxis-label',
                    },
                    offsetX: 0,
                    offsetY: 0,
                },

            },
            xaxis: {
                type: 'category',
                categories: ['Negetive', 'Neutral', 'Possitive'],
                labels: {
                    show: true,
                    style: {
                        fontSize: '12px',
                        fontFamily: 'Roboto',
                        fontWeight: 400,
                        cssClass: 'apexcharts-xaxis-label',
                    },
                    offsetX: 0,
                    offsetY: 0,
                },
            },
            tooltip: {
                y: {
                    formatter: function (val: string) {
                        return val + "%"
                    }
                },
            },
            legend: {
                fontSize: '12px',
                fontFamily: 'Roboto',
                fontWeight: 400,
            }
        }
    }

    render() {
        return (
            <div className='contain'>
                <Paper className='chart-section'>
                    <div className='title'>
                        Review Sentiment Analysis Report
                    </div>
                    <ReactApexChart options={this.state.options} series={this.state.series} type="bar" height={350} width={600} />
                </Paper>
            </div>
           
        )
    }
}
