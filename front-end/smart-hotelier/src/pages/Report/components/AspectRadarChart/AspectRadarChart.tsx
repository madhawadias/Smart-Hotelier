import { Paper } from '@material-ui/core'
import React, { Component } from 'react'
import ReactApexChart from 'react-apexcharts'

import './AspectRadarChart.scss'

export default class AspectRadarChart extends Component<{ theme: string }> {
    state = {

        series: [{
            name: 'Kingsbury',
            data: [80, 50, 30, 40, 100],
        }, {
            name: 'Galadari',
            data: [20, 30, 40, 80, 20],
        }],
        options: {
            theme: {
                mode: this.props.theme
            },
            colors: ['#00667C', '#7B178B'],
            chart: {
                height: 350,
                type: 'radar',
                dropShadow: {
                    enabled: true,
                    blur: 1,
                    left: 1,
                    top: 1
                }
            },
            stroke: {
                width: 2
            },
            fill: {
                opacity: 0.1
            },
            markers: {
                size: 0
            },
            yaxis: {
                show: false
            },
            xaxis: {
                categories: ['Staff', 'Location', 'Food', 'Room', 'Value for money']
            },
            legend: {
                fontSize: '12px',
                fontFamily: 'Roboto',
                fontWeight: 400,
            }
        },


    };

    render() {
        return (
            <div className='contain'>
                <Paper className='chart-section'>
                    <div className='title'>
                        Aspect Analysis Report
                    </div>
                    <ReactApexChart options={this.state.options} series={this.state.series} type="radar" height={350} width={600} />
                </Paper>
            </div>
            
        )
    }
}
