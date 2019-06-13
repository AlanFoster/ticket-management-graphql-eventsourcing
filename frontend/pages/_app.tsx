import React from 'react';
import App, { Container } from 'next/app';
import Page from "../src/page";

class MyApp extends App {
    static async getInitialProps({ Component, ctx }) {
        let pageProps = {};
        if (Component.getInitialProps) {
            pageProps = await Component.getInitialProps(ctx);
        }
        // this exposes the query to the user
        pageProps.query = ctx.query;
        return { pageProps };
    }

    componentDidMount() {
        // Remove the server-side injected CSS.
        const jssStyles = document.querySelector('#jss-server-side');
        if (jssStyles) {
            jssStyles.parentNode.removeChild(jssStyles);
        }
    }

    render() {
        const { Component, pageProps } = this.props;

        return (
            <Container>
                <Page>
                    <Component {...pageProps} />
                </Page>
            </Container>
        );
    }
}

export default MyApp;
