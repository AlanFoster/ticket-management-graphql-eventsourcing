import React from 'react';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import {makeStyles} from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import ButtonLink from '../../src/button-link'

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

const list = [
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

export default function List() {
    const classes = useStyles();

    return (
        <Container className={classes.cardGrid} maxWidth="md">
            <Grid container spacing={4}>
                {list.map(ticket => (
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
                                        query: { id: ticket.id }
                                    }}
                                    size="small"
                                    color="primary"
                                >
                                    View
                                </ButtonLink>
                                <Button size="small" color="secondary">
                                    Delete
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </Container>
    );
}
