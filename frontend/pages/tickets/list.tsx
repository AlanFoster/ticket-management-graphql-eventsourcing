import React from 'react';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import {makeStyles} from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import ButtonLink from '../../src/button-link'
import gql from "graphql-tag";
import {Query} from "react-apollo";
import {DeleteTicket} from "../../src/components/tickets/delete-button";
import * as GetTicketsTypes from "./__generated__/getTickets";

const useStyles = makeStyles(theme => ({
    cardGrid: {
    },
    card: {
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
    },
    cardMedia: {
        paddingTop: '56.25%', // 16:9
    },
    cardContent: {
        flexGrow: 1,
    },
}));

export const GET_TICKETS = gql`
    query getTickets {
       tickets {
           id
           name
           updatedAt
       } 
    }
`;

export default function List() {
    const classes = useStyles();

    return (
        <Query<GetTicketsTypes.getTickets, never>
            query={GET_TICKETS}
        >
            {({ loading, error, data }) => {
                if (loading) return "Loading...";
                if (error) return `Error! ${error.message}`;

                return (
                    <Container className={classes.cardGrid} maxWidth="md">
                        <Grid container spacing={4}>
                            {data.tickets.map(ticket => (
                                <Grid item key={ticket.id} xs={12} sm={6} md={4}>
                                    <Card className={classes.card}>
                                        <CardContent className={classes.cardContent}>
                                            <Typography gutterBottom variant="h5" component="h2">
                                                {ticket.name}
                                            </Typography>
                                        </CardContent>
                                        <CardActions>
                                            <ButtonLink
                                                href={{
                                                    pathname: '/tickets/show',
                                                    query: {id: ticket.id}
                                                }}
                                                size="small"
                                                color="primary"
                                            >
                                                View
                                            </ButtonLink>
                                            <DeleteTicket
                                                id={ticket.id}
                                            />
                                        </CardActions>
                                    </Card>
                                </Grid>
                            ))}
                        </Grid>
                    </Container>
                );
            }}
        </Query>
    );
}
