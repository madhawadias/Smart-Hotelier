import { Button, Typography,Paper } from '@material-ui/core';
import Box from '@material-ui/core/Box';
import CircularProgress, { CircularProgressProps } from '@material-ui/core/CircularProgress';
import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import './LoadingPage.scss'

function CircularProgressWithLabel(props: CircularProgressProps & { value: number }) {
    return (
        <Box position="relative" display="inline-flex">
            <CircularProgress variant="static" {...props} size={160} thickness={1}/>
            <Box
                top={0}
                left={0}
                bottom={0}
                right={0}
                position="absolute"
                display="flex"
                alignItems="center"
                justifyContent="center"
            >
                <Typography variant="h3" component="div" color="textPrimary">{`${Math.round(
                    props.value,
                )}%`}</Typography>
            </Box>
        </Box>
    );
}

export default class LoadingPage extends Component {
    state={
        progress:90,
    }

    render() {
        const progress = this.state.progress
        return (
            <div>
            <Paper className='head'>
                The Kingsbury Colombo,Sri Lanka  vs  Hotel The Galadari, Colombo, Sri Lanka
            </Paper>

            <Paper className='section'>
                <div className='title'>
                    YOUR ANALYTIC REPORT IS GENERATING
                </div>

                <div className='progress'>
                    <div className='precentage'>
                        <CircularProgressWithLabel value={progress}/>
                    </div>

                    <div className='completed'>
                        <Link to='/report'>
                            completed
                        </Link>
                    </div>
                </div>
                
                <div className='cancel'>
                    <Button className='cancelButton' variant="contained" color="primary" onClick={(e) => {
                        e.preventDefault();
                        window.location.href = '/';
                    }}>CANCEL</Button>
                </div>
            </Paper>
            </div>
        )
    }
}
