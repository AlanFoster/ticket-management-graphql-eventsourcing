import * as React from "react";
import {makeStyles} from "@material-ui/core";

const useSkeletonStyles = makeStyles(theme => ({
    root: {

    },
    '@keyframes skeleton-animation': {
        '0%': {
            backgroundPosition: '-200px 0'
        },
        '100%': {
            backgroundPosition: 'calc(200px + 100%) 0'
        }
    },
    element: {
        ...theme.typography.h3,
        height: '1em',
        width: '100%',
        display: 'inline-block',
        background: '#eee',
        backgroundImage: 'linear-gradient(90deg, #eee, #f5f5f5, #eee)',
        backgroundSize: '200px 100%',
        borderRadius: '4px',
        backgroundRepeat: 'no-repeat',
        animation: '$skeleton-animation 1.2s ease-in-out infinite'
    }
}));

export const Placeholder = function ({ count = 1 }) {
    const classes = useSkeletonStyles();
    const elements = [];
    for (var i = 0; i < count; i++) {
        elements.push(<span key={i} className={classes.element} />)
    }

    return (
        <div className={classes.root}>
            {elements}
        </div>
    );
};
