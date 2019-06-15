import * as React from "react";
import {makeStyles, Paper, Typography, Grid, Button} from "@material-ui/core";
import {CreateTicketDialog} from "./create-ticket-dialog";

const useStyles = makeStyles(theme => ({
    root: {
        padding: theme.spacing(2),
    },
}));

export const NoTickets = function () {
    const classes = useStyles();

    return (
        <Paper className={classes.root}>
            <Grid container direction="column" justify="space-around"  alignItems="center" className={classes.root} spacing={3}>
                <Grid item>
                    <Typography variant="h5" component="h3">
                        Nothing here yet!
                    </Typography>
                </Grid>
                <Grid item>
                    <Typography component="p">
                        Get started and create some tickets
                    </Typography>
                </Grid>
                <Grid item>
                    <CreateTicketDialog />
                </Grid>
            </Grid>
        </Paper>
    )
};
