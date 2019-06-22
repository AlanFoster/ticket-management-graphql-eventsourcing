import * as React from "react";
import { Mutation } from "react-apollo";
import gql from "graphql-tag";
import Router from "next/router";
import { GET_TICKETS } from '../../../pages/tickets/list';
import * as CloneTicketTypes from "./__generated__/cloneTicket";
import {Button} from "@material-ui/core";

const CLONE_TICKET = gql`
    mutation cloneTicket($id: ID!) {
        cloneTicket(id: $id) {
            ok
            ticket {
                id
            }
        }
    }
`;

function routeToTicket(ticket) {
    Router.push({
        pathname: '/tickets/show',
        query: {
            id: ticket.id
        }
    })
}

export const CloneTicket = function ({ id, ...buttonProps }) {
    return (
        <Mutation<CloneTicketTypes.cloneTicket, CloneTicketTypes.cloneTicketVariables>
            mutation={CLONE_TICKET}
            variables={{ id }}
            refetchQueries={[{ query: GET_TICKETS }]}
            awaitRefetchQueries={true}
            onCompleted={(data) => {
                routeToTicket(data.cloneTicket.ticket);
            }}
        >
            {(cloneTicket, { loading, error }) => (
                <Button
                    size="small"
                    color="primary"
                    disabled={loading || buttonProps.disabled}
                    onClick={() => cloneTicket()}
                >
                    Clone
                </Button>
            )}
        </Mutation>
    )
};
