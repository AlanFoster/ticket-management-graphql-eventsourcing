import React from "react";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import { makeStyles } from "@material-ui/core/styles";
import { EditableTextInput } from "../../src/components/editable-text-input";
import gql from "graphql-tag";
import { Mutation, Query } from "react-apollo";
import { DeleteTicket } from "../../src/components/tickets/delete-button";
import * as GetTicketTypes from "./__generated__/getTicket";
import * as RenameTicketTypes from "./__generated__/renameTicket";
import * as UpdateTicketDescriptionTypes from "./__generated__/updateTicketDescription";
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

const RENAME_TICKET = gql`
    mutation renameTicket($id: ID!, $name: String!) {
        renameTicket(id: $id, name: $name) {
            ok
        }
    }
`;

const UPDATE_TICKET_DESCRIPTION = gql`
    mutation updateTicketDescription($id: ID!, $description: String!) {
        updateTicketDescription(id: $id, description: $description) {
            ok
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
                                    <Mutation<
                                            RenameTicketTypes.renameTicket,
                                            RenameTicketTypes.renameTicketVariables
                                        >
                                        mutation={RENAME_TICKET}
                                    >
                                        {(renameTicket, { loading, error }) => (
                                            <EditableTextInput
                                                key={data.ticket.name}
                                                value={data.ticket.name}
                                                disabled={loading}
                                                onChange={name => {
                                                    renameTicket({
                                                        variables: {
                                                            id: data.ticket.id,
                                                            name: name
                                                        },
                                                        optimisticResponse: {
                                                            renameTicket: {
                                                                __typename: "RenameTicket",
                                                                ok: true
                                                            }
                                                        },
                                                        update: proxy => {
                                                            proxy.writeQuery({
                                                                query: GET_TICKET,
                                                                data: {
                                                                    ticket: {
                                                                        ...data.ticket,
                                                                        name: name
                                                                    }
                                                                }
                                                            });
                                                        }
                                                    });
                                                }}
                                            />
                                        )}
                                    </Mutation>
                                )}

                                {loading ? (
                                    <Placeholder />
                                ) : (
                                    <Mutation<
                                            UpdateTicketDescriptionTypes.renameTicket,
                                            UpdateTicketDescriptionTypes.renameTicketVariables
                                        >
                                        mutation={UPDATE_TICKET_DESCRIPTION}
                                    >
                                        {(updateTicketDescription, { loading, error }) => (
                                            <EditableTextInput
                                                key={data.ticket.description}
                                                value={data.ticket.description}
                                                multiline
                                                rows={4}
                                                disabled={loading}
                                                onChange={description => {
                                                    updateTicketDescription({
                                                        variables: {
                                                            id: data.ticket.id,
                                                            description: description
                                                        },
                                                        optimisticResponse: {
                                                            updateTicketDescription: {
                                                                __typename: "UpdateTicketDescription",
                                                                ok: true
                                                            }
                                                        },
                                                        update: proxy => {
                                                            proxy.writeQuery({
                                                                query: GET_TICKET,
                                                                data: {
                                                                    ticket: {
                                                                        ...data.ticket,
                                                                        description: description
                                                                    }
                                                                }
                                                            });
                                                        }
                                                    });
                                                }}
                                            />
                                        )}
                                    </Mutation>
                                )}
                            </CardContent>
                            <CardActions>
                                <CardActions>
                                    <Button size="small" color="primary" disabled={loading}>
                                        View History
                                    </Button>
                                    <DeleteTicket
                                        id={loading ? -1 : data.ticket.id}
                                        disabled={loading}
                                    />
                                </CardActions>
                            </CardActions>
                        </Card>
                    </React.Fragment>
                );
            }}
        </Query>
    );
}
