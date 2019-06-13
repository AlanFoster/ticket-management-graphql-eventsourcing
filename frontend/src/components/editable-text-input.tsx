import * as React from "react";
import { useState } from "react";
import { InputBase, makeStyles } from "@material-ui/core";
import { fade } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
    text: {
        ...theme.typography.h5,
        border: 0,
        padding: '0.5rem',
        borderRadius: '5px',
        width: '100%',
        whiteSpace: 'nowrap',
        overflow: 'hidden',
        textOverflow: 'ellipse',
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

}));

export const EditableTextInput = function (props) {
    const classes = useStyles();
    const [isEditing, setEditing] = useState(false);
    const [value, setValue] = useState(props.value);

    const saveField = function () {
        const hasValueChanged = value !== props.value;
        if (hasValueChanged) {
            props.onChange(value);
        } else {
            setEditing(false);
        }
    };

    const onKeyUp = function (e) {
        if (e.key === 'Enter') {
            saveField();
        }
    };

    return (
        <React.Fragment>
            {!isEditing &&
                <div
                    className={classes.text}
                    onClick={() => setEditing(true)}
                >
                    {props.value}
                </div>
            }
            {isEditing &&
            <InputBase
                value={value}
                onChange={e => setValue(e.target.value)}
                onKeyPress={onKeyUp}
                classes={{
                    input: classes.text,
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
