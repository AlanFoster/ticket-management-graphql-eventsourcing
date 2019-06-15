import React from "react";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import { makeStyles } from "@material-ui/core/styles";
import { EditableTextInput } from "../../src/components/editable-text-input";
import gql from "graphql-tag";
import { Query } from "react-apollo";
import { DeleteTicket } from "../../src/components/tickets/delete-button";
import * as GetTicketTypes from "./__generated__/getTicket";
import { Placeholder } from "../../src/components/placeholder";

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

const GET_TICKET = gql`
    query getTicket($id: ID!) {
        ticket(id: $id) {
            id
            name
            description
            updatedAt
        }
    }
`;

export default function Show(props) {
    const classes = useStyles();
    const { id } = props.query;

    return (
        <Query<GetTicketTypes.getTicket, GetTicketTypes.getTicketVariables>
            query={GET_TICKET}
            variables={{ id }}
        >
            {({ loading, error, data }) => {
                if (error) return `Error! ${error.message}`;

                return (
                    <React.Fragment>
                        <Card className={classes.card}>
                            <CardContent className={classes.cardContent}>
                                {loading ? (
                                    <Placeholder />
                                ) : (
                                    <EditableTextInput
                                        key={data.ticket.name}
                                        value={data.ticket.name}
                                        onChange={name => {
                                            /* noop */
                                        }}
                                    />
                                )}

                                {loading ? (
                                    <Placeholder />
                                ) : (
                                    <EditableTextInput
                                        key={data.ticket.description}
                                        value={data.ticket.description}
                                        multiline
                                        rows={4}
                                        onChange={name => {
                                            /* noop */
                                        }}
                                    />
                                )}
                            </CardContent>
                            <CardActions>
                                <CardActions>
                                    <Button size="small" color="primary" disabled={loading}>
                                        View History
                                    </Button>
                                    <DeleteTicket id={loading ? -1 : data.ticket.id} disabled={loading} />
                                </CardActions>
                            </CardActions>
                        </Card>
                    </React.Fragment>
                );
            }}
        </Query>
    );
}
