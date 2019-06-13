import React from 'react';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import {makeStyles} from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { EditableTextInput } from "../../src/components/editable-text-input";

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

export default function Show(props) {
    const classes = useStyles();
    const ticket = getTicket(props.query.id);

    return (
        <Container className={classes.cardGrid} maxWidth="md">
            <Card className={classes.card}>
                <CardContent className={classes.cardContent}>
                    <EditableTextInput
                        key={ticket.name}
                        value={ticket.name}
                        onChange={name => {/* noop */}}
                    />
                </CardContent>
                <CardActions>
                    <CardActions>
                        <Button size="small" color="primary">
                            View History
                        </Button>
                        <Button size="small" color="secondary">
                            Delete
                        </Button>
                    </CardActions>
                </CardActions>
            </Card>
        </Container>
    );
}
