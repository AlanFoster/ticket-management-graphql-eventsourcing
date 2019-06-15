# Ticket Management

Create, Edit, Delete, Duplicate tickets in a simple ticket management system - all managed by Event Sourcing.

## Running

First ensure that you have your `.env` file set up with the correct environment variables:

```
cp .env.example .env
```

Run the containers:

```
docker-compose build
docker-compose up
```

In a new tab, ensure that the database migrations have been applied:

```
docker-compose exec backend flask db upgrade
```

## Backend Dev

The development flow consists of running the docker containers with `docker-compose up`. Any changes to the `backend/` folder
will cause a reload of flask.

It is possible to start a new shell into the backend process with:

```
docker-compose exec backend /bin/sh
```

Running tests:

```
docker-compose exec backend /bin/sh
pytest
```

### Migrations

To create migration scripts, ensure that you have added/upgraded your SqlAchemy db models then create a new migration with:

```
flask db migrate -m "add event sourcing table"
```

To apply changes to your database:

```
flask db upgrade
```

## Frontend Dev

Running tests:

```
docker-compose exec frontend /bin/sh
yarn test
```

Ensuring GraphQL types are generated:

```
yarn codegen:watch
```

Downloading the latest schema from the backend:

```
yarn schema:fetch
```