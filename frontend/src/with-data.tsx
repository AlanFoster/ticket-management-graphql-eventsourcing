import withApollo from 'next-with-apollo';
import {InMemoryCache} from 'apollo-cache-inmemory';
import {ApolloClient} from 'apollo-client';
import {HttpLink} from 'apollo-link-http';

export const createApolloClient = function () {
    const cache = new InMemoryCache();
    const link = new HttpLink({
        uri: 'http://localhost:5000/graphql'
    });

    return new ApolloClient({
        cache,
        link
    });
};

export const withData = withApollo(createApolloClient, {
    getDataFromTree: "never"
});
