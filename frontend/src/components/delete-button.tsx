import React, {useState} from "react";
import {Dialog, Button, DialogActions, DialogContent, DialogContentText, DialogTitle} from "@material-ui/core";

export const DeleteButton = function (props) {
    const { onConfirm, ...buttonProps } = props;
    const [isOpen, setModalOpen] = useState(false);
    const handleModalOpen = () => {
        setModalOpen(true);
    };

    const handleModalClose = () => {
        setModalOpen(false);
    };

    return (
        <React.Fragment>
            <Button
                color="secondary"
                {...buttonProps}
                onClick={handleModalOpen}
            >
                Delete
            </Button>

            <Dialog
                open={isOpen}
                fullWidth={true}
                onClose={handleModalClose}
            >
                <DialogTitle>
                    Confirm deletion
                </DialogTitle>


                <DialogContent>
                    <DialogContentText>
                        Are you sure you want to delete this?
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button
                        size="small"
                        focused
                        color="secondary"
                        onClick={onConfirm}
                    >
                        Confirm
                    </Button>
                    <Button
                        size="small"
                        color="primary"
                        onClick={handleModalClose}
                    >
                        Cancel
                    </Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    );
}
