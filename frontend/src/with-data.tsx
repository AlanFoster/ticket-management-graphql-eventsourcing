import withApollo from 'next-with-apollo';
import {InMemoryCache} from 'apollo-cache-inmemory';
import {ApolloClient} from 'apollo-client';
import {HttpLink} from 'apollo-link-http';
import { IntrospectionFragmentMatcher } from 'apollo-cache-inmemory';
import introspectionQueryResultData from './../__generated__/fragmentTypes';

export const createApolloClient = function () {
    const fragmentMatcher = new IntrospectionFragmentMatcher({
        introspectionQueryResultData
    });

    const cache = new InMemoryCache({
        fragmentMatcher
    });
    const link = new HttpLink({
        uri: 'http://localhost:5511/graphql'
    });

    return new ApolloClient({
        cache,
        link
    });
};

export const withData = withApollo(createApolloClient, {
    getDataFromTree: "never"
});
