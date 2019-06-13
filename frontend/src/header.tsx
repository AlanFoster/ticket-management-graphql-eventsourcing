import * as React from "react";
import NotificationsIcon from '@material-ui/icons/Add';
import { AppBar, IconButton, makeStyles, Toolbar, Typography } from "@material-ui/core";
import { CreateTicketModal } from "./components/tickets/create";
import { Link } from './links';

const useStyles = makeStyles(theme => ({
    title: {
        flexGrow: 1,
    },
}));

export default function Header() {
    const classes = useStyles();
    const [isModalOpen, setModalOpen] = React.useState(false);
    const handleModalOpen = () => {
        setModalOpen(true);
    };

    const handleModalClose = () => {
        setModalOpen(false);
    };

    return (
        <AppBar position="relative">
            <CreateTicketModal
                open={isModalOpen}
                onClose={handleModalClose}
            />

            <Toolbar>
                <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
                    <Link href="/" color="inherit">
                        Tickets
                    </Link>
                </Typography>

                <IconButton
                    onClick={handleModalOpen}
                    aria-label="Add ticket"
                    data-testid="add-ticket"
                    color="inherit"
                >
                    <NotificationsIcon />
                </IconButton>
            </Toolbar>
        </AppBar>
    )
}
