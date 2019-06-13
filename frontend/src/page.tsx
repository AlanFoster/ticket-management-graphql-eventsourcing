import * as React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';
import Header from './header';
import {makeStyles} from "@material-ui/core";

const useStyles = makeStyles(theme => ({
   container: {
       paddingTop: theme.spacing(6),
       paddingBottom: theme.spacing(6),
   }
}));

export default function Page({ children }) {
    const classes = useStyles();

    return (
        <React.Fragment>
            <CssBaseline />
            <Header />
            <main>
                <Container className={classes.container}>
                    {children}
                </Container>
            </main>
        </React.Fragment>
    );
}
