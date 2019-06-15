import * as React from "react";
import { AppBar, makeStyles, Toolbar, Typography } from "@material-ui/core";
import { CreateTicketButton } from "./components/tickets/create-button";
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
            <Toolbar>
                <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
                    <Link href="/" color="inherit">
                        Tickets
                    </Link>
                </Typography>
                <CreateTicketButton />
            </Toolbar>
        </AppBar>
    )
}
