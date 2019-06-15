import * as React from "react";
import { useState } from "react";
import {InputBase, makeStyles, TextField, Typography} from "@material-ui/core";
import { fade } from "@material-ui/core/styles";
import clsx from "clsx";

const useStyles = makeStyles(theme => ({
    root: {
        padding: 0
    },
    text: {
        border: 0,
        padding: '0.5rem',
        borderRadius: '5px',
        width: '100%',
        lineHeight: 1.5,
        whiteSpace: 'pre-wrap',
        height: 'inherit',
        '&:hover': {
            transition: theme.transitions.create(['background-color', 'box-shadow'], { duration: 300 }),
            backgroundColor: '#f1f1f0',
        },
        '&:focus': {
            backgroundColor: '#fcfcfb',
            boxShadow: `${fade(theme.palette.primary.main, 0.25)} 0 0 0 2px`,
        },
    },
    singleline: {
        ...theme.typography.h5,
    },
    multiline: {
        lineHeight: 1.5,
    },
}));

export const EditableTextInput = function (props) {
    const classes = useStyles();
    const [isEditing, setEditing] = useState(false);
    const [value, setValue] = useState(props.value);

    const { multiline, rows } = props;

    const saveField = function () {
        const hasValueChanged = value !== props.value;
        if (hasValueChanged) {
            props.onChange(value);
        } else {
            setEditing(false);
        }
    };

    const onKeyUp = function (e) {
        if (!multiline && e.key === 'Enter') {
            saveField();
        }
    };

    const className = clsx({
        [classes.text]: true,
        [classes.multiline]: multiline,
        [classes.singleline]: !multiline,
    });

    return (
        <React.Fragment>
            {!isEditing &&
                <div className={classes.root}>
                    <Typography
                        className={className}
                        onClick={() => setEditing(true)}
                    >
                        {props.value}
                    </Typography>
                </div>
            }
            {isEditing &&
                <InputBase
                    value={value}
                    onChange={e => setValue(e.target.value)}
                    multiline={multiline}
                    onKeyPress={onKeyUp}
                    rows={
                        rows || value.split('\n').length
                    }
                    rowsMax={5}
                    classes={{
                        root: classes.root,
                        input: className,
                    }}
                    inputProps={{
                        onBlur: saveField,
                    }}
                    required
                    fullWidth={true}
                    autoFocus
                />
            }
        </React.Fragment>
    )
};
