/* eslint-disable jsx-a11y/anchor-has-content */
import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { withRouter } from 'next/router';
import NextLink from 'next/link';
import {Link as MuiLink, Button as MuiButton, IconButton as MuiIconButton} from "@material-ui/core";

const NextComposed = React.forwardRef(function NextComposed(props, ref) {
    const { as, href, prefetch, ...other } = props;

    return (
        <NextLink href={href} prefetch={prefetch} as={as}>
            <a ref={ref} {...other} />
        </NextLink>
    );
});

NextComposed.propTypes = {
    as: PropTypes.string,
    href: PropTypes.string,
    prefetch: PropTypes.bool,
};

// A styled version of the Next.js Link component:
// https://nextjs.org/docs/#with-link
function NextAwareLink(props) {
    const { activeClassName, router, className: classNameProps, innerRef, naked, component: Component, ...other } = props;

    const className = clsx(classNameProps, {
        [activeClassName]: router.pathname === props.href && activeClassName,
    });

    if (naked) {
        return <NextComposed className={className} ref={innerRef} {...other} />;
    }

    return <Component component={NextComposed} className={className} ref={innerRef} {...other} />;
}

NextAwareLink.propTypes = {
    activeClassName: PropTypes.string,
    as: PropTypes.string,
    className: PropTypes.string,
    href: PropTypes.string,
    innerRef: PropTypes.oneOfType([PropTypes.func, PropTypes.object]),
    naked: PropTypes.bool,
    onClick: PropTypes.func,
    prefetch: PropTypes.bool,
    router: PropTypes.shape({
        pathname: PropTypes.string.isRequired,
    }).isRequired,
};

NextAwareLink.defaultProps = {
    activeClassName: 'active',
};

const RouterLink = withRouter(NextAwareLink);

export const Link = React.forwardRef((props, ref) => <RouterLink {...props} innerRef={ref} component={MuiLink} />);
export const ButtonLink = React.forwardRef((props, ref) => <RouterLink {...props} innerRef={ref} component={MuiButton} />);
export const IconButtonLink = React.forwardRef((props, ref) => <RouterLink {...props} innerRef={ref} component={MuiIconButton} />);
