import React from "react";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import ButtonLink from "../../src/button-link";
import gql from "graphql-tag";
import { Query } from "react-apollo";
import { DeleteTicket } from "../../src/components/tickets/delete-button";
import * as GetTicketsTypes from "./__generated__/getTickets";
import { NoTickets } from "../../src/components/tickets/no-tickets";
import { CreateTicketDialog } from "../../src/components/tickets/create-ticket-dialog";

const useStyles = makeStyles(theme => ({
    card: {
        height: "100%",
        display: "flex",
        flexDirection: "column"
    },
    cardMedia: {
        paddingTop: "56.25%" // 16:9
    },
    cardContent: {
        flexGrow: 1
    }
}));

export const GET_TICKETS = gql`
    query getTickets {
        tickets {
            id
            name
            description
            updatedAt
        }
    }
`;

const ListHeading = function() {
    return (
        <Grid container spacing={4} justify="space-between">
            <Grid item>
                <Typography variant="h5" component="h3">
                    Your tickets
                </Typography>
            </Grid>
            <Grid item>
                <CreateTicketDialog />
            </Grid>
        </Grid>
    );
};

const Tickets = function({
                             tickets
                         }: {
    tickets: GetTicketsTypes.getTickets_tickets[];
}) {
    const classes = useStyles();
    return (
        <Grid container spacing={4}>
            {tickets.map(ticket => (
                <Grid item key={ticket.id} xs={12} sm={6} md={4}>
                    <Card className={classes.card}>
                        <CardContent className={classes.cardContent}>
                            <Typography noWrap gutterBottom variant="h5" component="h2">
                                {ticket.name}
                            </Typography>
                            <Typography component="p">
                                {ticket.description}
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <ButtonLink
                                href={{
                                    pathname: "/tickets/show",
                                    query: { id: ticket.id }
                                }}
                                size="small"
                                color="primary"
                            >
                                View
                            </ButtonLink>
                            <DeleteTicket id={ticket.id} />
                        </CardActions>
                    </Card>
                </Grid>
            ))}
        </Grid>
    );
};

export default function List() {
    return (
        <Query<GetTicketsTypes.getTickets, never> query={GET_TICKETS}>
            {({ loading, error, data }) => {
                if (loading) return "Loading...";
                if (error) return `Error! ${error.message}`;

                return (
                    <Grid container direction="column" spacing={3}>
                        <Grid item>
                            <ListHeading />
                        </Grid>
                        <Grid item>
                            {data.tickets.length === 0 ? (
                                <NoTickets />
                            ) : (
                                <Tickets tickets={data.tickets} />
                            )}
                        </Grid>
                    </Grid>
                );
            }}
        </Query>
    );
}
