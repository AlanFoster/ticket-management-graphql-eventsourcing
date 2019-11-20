module.exports = {
    client: {
        includes: [
            '{src,pages}/**/*.{ts,tsx,js,jsx}',
        ],
        service: {
            name: 'backend',
            url: 'http://localhost:5511/graphql'
        },
    },
};
