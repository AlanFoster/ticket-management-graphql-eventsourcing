import React from 'react';
import {
    Avatar,
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    List, ListItem, ListItemAvatar, ListItemText,
    makeStyles,
    Typography
} from "@material-ui/core";
import AssignmentIcon from '@material-ui/icons/Assignment';
import NoteAddIcon from '@material-ui/icons/NoteAdd';
import * as GetTicketTypes from "../../../pages/tickets/__generated__/getTicket";
import { green } from '@material-ui/core/colors';
import {Link} from "../../links";

const useStyles = makeStyles(theme => ({
    paper: {
        padding: theme.spacing(3, 0, 0, 0),
    },
    updatedAvatar: {
        color: '#fff',
        backgroundColor: green[500],
    },
    block: {
        display: 'block'
    }
}));

type Props = {
    history: GetTicketTypes.getTicket_ticket_history[];
};

type HistoryListItemTextProps = {
    item: GetTicketTypes.getTicket_ticket_history
}

const HistoryListItem: React.FC<HistoryListItemTextProps> = function ({ item }) {
    const classes = useStyles();
    switch (item.__typename) {
        case "TicketFieldUpdated":
            return (
                <React.Fragment>
                    <ListItemAvatar>
                        <Avatar className={classes.updatedAvatar}>
                            <AssignmentIcon />
                        </Avatar>
                    </ListItemAvatar>
                    <ListItemText
                        primary={
                            <React.Fragment>
                                <Typography
                                    component="span"
                                    color="textPrimary"
                                >
                                    Ticket {item.field} updated
                                </Typography>
                                {' '}
                                <Typography
                                    component="span"
                                    variant="body2"
                                    color="textSecondary"
                                >
                                    {item.timestamp}
                                </Typography>
                            </React.Fragment>
                        }
                        secondary={
                            <React.Fragment>
                                Old {item.field}:
                                <Typography
                                    component="span"
                                    variant="body2"
                                    className={classes.block}
                                    color="textPrimary"
                                >
                                    {item.oldValue}
                                </Typography>
                                New {item.field}:
                                <Typography
                                    component="span"
                                    variant="body2"
                                    className={classes.block}
                                    color="textPrimary"
                                >
                                    {item.newValue}
                                </Typography>
                            </React.Fragment>
                        }
                    />
                </React.Fragment>
            );
        case "TicketCloned":
            return (
                <React.Fragment>
                    <ListItemAvatar>
                        <Avatar className={classes.updatedAvatar}>
                            <NoteAddIcon />
                        </Avatar>
                    </ListItemAvatar>
                    <ListItemText
                        primary={
                            <React.Fragment>
                                <Typography
                                    component="span"
                                    color="textPrimary"
                                >
                                    Ticket cloned from{' '}
                                    <Link
                                        href={{
                                            pathname: "/tickets/show",
                                            query: { id: item.originalTicketId }
                                        }}
                                    >
                                        {item.originalTicketName}
                                    </Link>.
                                </Typography>
                                {' '}
                                <Typography
                                    component="span"
                                    variant="body2"
                                    color="textSecondary"
                                >
                                    {item.timestamp}
                                </Typography>
                            </React.Fragment>
                        }
                    />
                </React.Fragment>
            )
    }
}

export const ViewHistoryButton: React.FC<Props> = function (props) {
    const classes = useStyles();
    const [isModalOpen, setModalOpen] = React.useState(false);
    const handleModalOpen = () => {
        setModalOpen(true);
    };

    const handleModalClose = () => {
        setModalOpen(false);
    };

    return (
        <React.Fragment>
            <Button
                onClick={handleModalOpen}
                aria-label="Add ticket"
                data-testid="add-ticket"
                color="primary"
                disabled={props.disabled}
            >
                View History
            </Button>

            <Dialog
                open={isModalOpen}
                fullWidth={true}
                classes={{ paper: classes.paper }}
                onClose={handleModalClose}
            >
                <DialogContent>
                    {props.history.length === 0 && (
                        'No changes yet!'
                    )}

                    {props.history.length > 0 && (
                        <List>
                            {props.history.map(function (item, index) {
                                return (
                                    <ListItem key={index} alignItems='flex-start'>
                                        <HistoryListItem item={item} />
                                    </ListItem>
                                );
                            })}
                        </List>
                    )}
                </DialogContent>
                <DialogActions>
                    <Button
                        size="small"
                        color="primary"
                        onClick={handleModalClose}
                    >
                        Done
                    </Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    )
}
