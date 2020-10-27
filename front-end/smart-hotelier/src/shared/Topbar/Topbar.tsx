import { Paper } from '@material-ui/core';
import React, { Component } from 'react';

import './Topbar.scss'

export default class Topbar extends Component {
    render() {
        return (
            <Paper className='pageHeader' square>
                <div className='logo'>
                    <img src='smart-hotelier-horizontal transparent.png'></img>
                </div>
                <div className="options">
                    <div className='user'>
                        <img src='user.png'></img>
                    </div>

                </div>
            </Paper>
        )
    }
}
