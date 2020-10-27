import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import './App.scss';
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
import CssBaseline from "@material-ui/core/CssBaseline";

import Page from './shared/Page/Page'
import LandingPage from './pages/Landing-page/LandingPage'
import LoadingPage from './pages/Loading-page/LoadingPage'
import Report from './pages/Report/report'

const defTheme='light'

const theme = createMuiTheme({
  palette: {
    type: defTheme,
    primary: {
      main: "#00667C"
    },
    success:{
      main:'#343434'
    }
  },
  typography: {
    fontFamily: 'Roboto'
  }
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Page theme={defTheme}>
          <Switch>
            <Route exact path='/' component={LandingPage} />
            <Route exact path='/loading' component={LoadingPage} />
            <Route exact path='/report' render={(props) => <Report theme={defTheme} {...props} />} />
          </Switch>
        </Page>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;