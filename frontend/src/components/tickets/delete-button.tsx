import * as React from "react";
import { DeleteButton } from "../delete-button";
import { Mutation } from "react-apollo";
import gql from "graphql-tag";
import Router from "next/router";
import { GET_TICKETS } from '../../../pages/tickets/list';
import * as DeleteTicketTypes from "./__generated__/deleteTicket";

const DELETE_TICKET = gql`
    mutation deleteTicket($id: ID!) {
        deleteTicket(id: $id) {
            ok
        }
    }
`;

function routeToTickets() {
    Router.push({
        pathname: '/tickets',
    });
}

export const DeleteTicket = function ({ id, ...buttonProps }) {
    return (
        <Mutation<DeleteTicketTypes.deleteTicket_deleteTicket, DeleteTicketTypes.deleteTicketVariables>
            mutation={DELETE_TICKET}
            variables={{ id }}
            refetchQueries={[{ query: GET_TICKETS }]}
            awaitRefetchQueries={true}
            onCompleted={() => {
                routeToTickets();
            }}
        >
            {(deleteTicket, { loading, error }) => (
                <DeleteButton
                    {...buttonProps}
                    size="small"
                    color="secondary"
                    disabled={loading || buttonProps.disabled}
                    onConfirm={deleteTicket}
                />
            )}
        </Mutation>
    )
};
