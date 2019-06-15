import React, {useReducer} from 'react';
import {EditableTextInput} from "../editable-text-input";
import {Button, Dialog, DialogActions, DialogContent, IconButton, makeStyles, Toolbar} from "@material-ui/core";
import gql from "graphql-tag";
import {Mutation} from "react-apollo";
import Router from 'next/router';
import {GET_TICKETS} from "../../../pages/tickets/list";
import NotificationsIcon from '@material-ui/icons/Add';

const CREATE_TICKET = gql`
    mutation createTicket($name: String!) {
        createTicket(name: $name) {
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

interface State {
    isOpen: boolean;
    name: string;
}

type Action =
    | { type: 'opened' }
    | { type: 'nameUpdated'; payload: string }
    | { type: 'completed' }
    | { type: 'closed' }

function initialState(): State {
    return {
        isOpen: false,
        name: 'Your ticket name'
    };
}

function reducer(state: State, action: Action) {
    switch (action.type) {
        case 'opened':
            return { ...initialState(), isOpen: true };
        case 'nameUpdated':
            return { ...state, name: action.payload };
        case 'completed':
            return { ...state, isOpen: false };
        case 'closed':
            return { ...state, isOpen: false };
        default:
            throw new Error();
    }
}

const useStyles = makeStyles(theme => ({
    paper: {
        padding: theme.spacing(3, 0, 0, 0),
    },
}));


export const CreateTicketContained = function (props) {
    return (
        <Button
            {...props}
            size="large"
            color="primary"
            variant="contained"
        >
            Create ticket
        </Button>
    )
};

export const CreateTicketIcon = function (props) {
    return (
        <IconButton
            {...props}
            color="inherit"
        >
            <NotificationsIcon />
        </IconButton>
    )
};

export const CreateTicketDialog = function (props) {
    const classes = useStyles();
    const OpenButton = props.openButton || CreateTicketContained;
    const [state, dispatch] = useReducer(reducer, initialState());

    return (
        <Mutation
            mutation={CREATE_TICKET}
            variables={{ name: state.name }}
            refetchQueries={[{ query: GET_TICKETS }]}
            awaitRefetchQueries={true}
            onCompleted={(data) => {
                dispatch({ type: 'completed' });
                routeToTicket(data.createTicket.ticket);
            }}
        >
            {(createTicket, { loading, error }) => (
                <React.Fragment>
                    <OpenButton
                        onClick={() => {
                            dispatch({type: 'opened'})
                        }}
                        aria-label="Add ticket"
                        data-testid="add-ticket"
                    />

                    <Dialog
                        open={state.isOpen}
                        fullWidth={true}
                        classes={classes}
                        onClose={() => {
                            dispatch({ type: 'closed' });
                        }}
                    >
                        <DialogContent>
                            <EditableTextInput
                                key={state.name}
                                value={state.name}
                                onChange={name => dispatch({ type: 'nameUpdated', payload: name })}
                            />
                        </DialogContent>
                        <DialogActions>
                            <Button
                                size="small"
                                color="primary"
                                onClick={createTicket}
                                disabled={loading}
                            >
                                Create
                            </Button>
                            <Button
                                size="small"
                                color="secondary"
                                onClick={() => {
                                    dispatch({ type: 'closed' });
                                }}
                            >
                                Cancel
                            </Button>
                        </DialogActions>
                    </Dialog>
                </React.Fragment>
            )}
        </Mutation>
    )
}
