import React, { Component } from 'react'

import './Page.scss';

import Topbar from '../Topbar/Topbar';
import Footer from '../Footer/Footer';

export default class Page extends Component<{theme:string}> {
    render() {
        return (
            <div className="page">
                <Topbar />

                <div className="pageContent">
                    {this.props.children}
                </div>
                <Footer/>
            </div>
        )
    }
}