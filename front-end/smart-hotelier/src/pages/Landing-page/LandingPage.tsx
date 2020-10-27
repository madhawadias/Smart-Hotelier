import { Button, IconButton, InputAdornment, TextField,Paper, ThemeProvider } from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';
import React, { Component } from 'react'
import './LandingPage.scss'

export default class LandingPage extends Component {

    state = {
        label: '',
        labels: []
    }

    handleChange = (property: string) => (event: any) => {
        this.setState({
            [property]: event.target.value
        })
        console.log(this.state.label)
    }

    removeLabel = (label: any) => {
        const { labels } = this.state;

        this.setState({
            labels: labels.filter(i => i !== label)
        })
    }

    onAdd = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        const { labels, label } = this.state;

        this.setState({
            labels: [...labels, label]
        });

    }

    getProperties() {
        const { labels } = this.state;

        if (labels.length) {
            return labels.map(i => {
                return (
                    <div className='resultBox' key={i}>
                        <div className='result'>
                            {i}
                        </div>
                        <Button className='removeButton'
                            variant="contained"
                            color="primary"
                            onClick={() => this.removeLabel(i)}>REMOVE</Button>
                    </div>

                )
            });
        }

    }
    render() {
        return (
            <Paper className='section'>

                <div className='title'>
                    Analyse Your Data
                </div>

                <div className='description'>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                    ut labore et dolore magna aliqua. Pretium lectus quam id leo in vitae turpis massa.
                    Risus sed vulputate odio ut enim. Aliquam ultrices sagittis orci a scelerisque purus semper eget.
                    Sem fringilla ut morbi tincidunt augue interdum velit euismod. Volutpat ac tincidunt vitae semper quis.
                    Suspendisse faucibus interdum posuere lorem ipsum dolor sit amet consectetur.
                    Arcu non odio euismod lacinia at quis risus sed.
                    Pellentesque adipiscing commodo elit at imperdiet dui accumsan sit.
                    Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.

                </div>

                <form className='searchBox' onSubmit={this.onAdd}>
                    <TextField
                        id="outlined-basic"
                        label="Search Your Data Set.."
                        onChange={this.handleChange('label')}
                        variant="outlined"
                        InputProps={{
                            endAdornment: (
                                <InputAdornment position="start">
                                    <IconButton>
                                        <SearchIcon />
                                    </IconButton>
                                </InputAdornment>
                            )
                        }}>
                        <SearchIcon />
                    </TextField>
                    <Button className='addButton'
                        variant="contained"
                        color="primary"
                        type="submit" >
                        ADD
                    </Button>
                </form>

                {this.getProperties()}

                <div className='generate'>
                    <Button className='generateButton'
                        variant="contained"
                        color="primary"
                        onClick={(e) => {
                            e.preventDefault();
                            window.location.href = '/loading';
                        }}>
                        GENERATE ANALYTICS
                    </Button>
                </div>
            </Paper>
        )
    }
}
