import React, {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {EditableTextInput} from "../editable-text-input";
import Button from "@material-ui/core/Button";
import {Dialog, DialogActions, DialogContent, DialogTitle} from "@material-ui/core";

const useStyles = makeStyles(theme => ({
    modal: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
    },
    paper: {
        position: 'absolute',
        width: 400,
        backgroundColor: theme.palette.background.paper,
        boxShadow: theme.shadows[5],
        padding: theme.spacing(4),
        outline: 'none',
    },
}));

export const CreateTicketModal = function ({ open, onClose, onCreate }) {
    const classes = useStyles();
    const [ticketName, setTicketName] = useState("Your ticket name");

    return (
        <Dialog
            aria-labelledby="create-ticket-dialog-title"
            open={open}
            fullWidth={true}
            onClose={onClose}
        >
            <DialogContent>
                <EditableTextInput
                    key={ticketName}
                    value={ticketName}
                    onChange={name => setTicketName(name)}
                />
            </DialogContent>

            <DialogActions>
                <Button size="small" color="primary" onCreate={onCreate}>
                    Create
                </Button>
                <Button size="small" color="secondary" onClick={onClose}>
                    Cancel
                </Button>
            </DialogActions>
        </Dialog>
    )
}
