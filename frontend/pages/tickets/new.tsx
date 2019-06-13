import React from 'react';
import {makeStyles} from '@material-ui/core/styles';
import ShowTicket from '../../src/components/tickets/show';

const useStyles = makeStyles(theme => ({
    cardGrid: {
        paddingTop: theme.spacing(8),
        paddingBottom: theme.spacing(8),
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

const tickets = [
    {
        id: '1',
        name: 'First ticket',
        updated_at: 123
    },
    {
        id: '2',
        name: 'Second ticket',
        updated_at: 1234
    },
];

const getTicket = function (id) {
    return tickets.find(ticket => ticket.id === id);
};

export default function Ticket(props) {
    const classes = useStyles();
    const ticket = {
        id: null,
        name: 'New ticket name',
        updated_at: null
    };

    return (
        <ShowTicket ticket={ticket} />
    );
}
