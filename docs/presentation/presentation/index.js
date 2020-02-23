// Import React
import React from "react";

// Import Spectacle Core tags
import {
  Appear,
  BlockQuote,
  Cite,
  CodePane,
  ComponentPlayground,
  Deck,
  Fill,
  Heading,
  Image,
  Layout,
  Link,
  ListItem,
  List,
  Quote,
  Slide,
  SlideSet,
  TableBody,
  TableHeader,
  TableHeaderItem,
  TableItem,
  TableRow,
  Table,
  Text
} from "spectacle";

// Import image preloader util
import preloader from "spectacle/lib/utils/preloader";

// Import theme
import createTheme from "spectacle/lib/themes/default";

// Require CSS
require("normalize.css");
require("spectacle/lib/themes/default/index.css");
require("codemirror/mode/jsx/jsx");
require("spectacle/lib/themes/default/dark.codemirror.css");

import WithSlidesLink from "./with-slides-link";

const images = {
  distilled: require("../assets/ddd-distilled.jpg"),
  projection: require("../assets/projection.png"),
  commandArchitecture: require("../assets/command-architecture.png"),
  queryArchitecture: require("../assets/query-architecture.png")
};

preloader(images);

const theme = createTheme(
  {
    primary: "white",
    secondary: "#1F2022",
    tertiary: "#03A9FC",
    quartenary: "#CECECE"
  },
  {
    primary: "Montserrat",
    secondary: "Helvetica"
  }
);

const tableStyles = {
  style: {
    border: "2px solid #aaa"
  }
};
const tableHighlightBackgroundColor = "#fca503";

const buttonStyles = {
  style: {
    padding: 20,
    background: "black",
    minWidth: 300,
    margin: 20,
    textTransform: "uppercase",
    border: "none",
    color: "white",
    outline: "none",
    fontWeight: "bold",
    fontSize: "1.5em"
  }
};

class SimpleDatabaseExample extends React.Component {
  constructor(props) {
    super(props);
    this.initialState = {
      simpleDatabase: {
        rows: []
      }
    };
    this.state = this.initialState;
  }

  createSimpleDatabaseRecord = () => {
    this.setState({
      simpleDatabase: {
        updateIndex: 0,
        highlighted: [
          "id",
          "name",
          "name",
          "description",
          "createdAt",
          "deletedAt"
        ],
        rows: [
          {
            id: 7,
            name: "1st name",
            description: "1st description",
            createdAt: new Date(),
            deletedAt: undefined
          }
        ]
      }
    });
  };

  updateSimpleDatabaseRecord = () => {
    const updateIndex = this.state.simpleDatabase.updateIndex;
    let highlighted = [];
    const newRecord = {
      ...this.state.simpleDatabase.rows[0]
    };

    switch (updateIndex) {
      case 0:
        newRecord.name = "2nd name";
        highlighted = ["name"];
        break;
      case 1:
        newRecord.name = "3rd name";
        highlighted = ["name"];
        break;
      case 2:
        newRecord.description = "2nd description";
        highlighted = ["description"];
        break;
      case 3:
        newRecord.description = "4th name";
        newRecord.description = "3rd description";
        highlighted = ["name", "description"];
        break;
    }

    this.setState({
      simpleDatabase: {
        updateIndex: updateIndex + 1,
        highlighted: highlighted,
        rows: [newRecord]
      }
    });
  };

  deleteSimpleDatabaseRecord = () => {
    const newRecord = {
      ...this.state.simpleDatabase.rows[0],
      deletedAt: new Date()
    };
    const highlighted = ["deletedAt"];

    this.setState({
      simpleDatabase: {
        updateIndex: 0,
        highlighted: highlighted,
        rows: [newRecord]
      }
    });
  };

  render() {
    return (
      <div>
        <Heading size={4} textColor="tertiary">
          Tickets Table
        </Heading>
        <div style={{ marginLeft: "-16rem", marginTop: "4rem" }}>
          <Table {...tableStyles}>
            <TableHeader>
              <TableRow>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 3rem" }}>id</div>
                </TableHeaderItem>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 5rem" }}>name</div>
                </TableHeaderItem>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 5rem" }}>description</div>
                </TableHeaderItem>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 3rem" }}>created_at</div>
                </TableHeaderItem>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 3rem" }}>deleted_at</div>
                </TableHeaderItem>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow {...tableStyles}>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
              </TableRow>
              {this.state.simpleDatabase.rows.map((row, id) => {
                const itemStyles = name => {
                  const isHighlighted =
                    this.state.simpleDatabase.highlighted.indexOf(name) > -1;
                  if (isHighlighted) {
                    return {
                      ...tableStyles,
                      style: {
                        ...tableStyles.style,
                        backgroundColor: tableHighlightBackgroundColor
                      }
                    };
                  }
                  return tableStyles;
                };

                return (
                  <TableRow key={id}>
                    <TableItem {...itemStyles("id")}>{row.id}</TableItem>
                    <TableItem {...itemStyles("name")}>{row.name}</TableItem>
                    <TableItem {...itemStyles("description")}>
                      {row.description}
                    </TableItem>
                    <TableItem {...itemStyles("createdAt")}>
                      {row.createdAt.toLocaleString("en-US", {
                        hour: "numeric",
                        minute: "numeric",
                        hour12: true
                      })}
                    </TableItem>
                    <TableItem {...itemStyles("deletedAt")}>
                      {row.deletedAt
                        ? row.deletedAt.toLocaleString("en-US", {
                            hour: "numeric",
                            minute: "numeric",
                            hour12: true
                          })
                        : ""}
                    </TableItem>
                  </TableRow>
                );
              })}

              <TableRow>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
                <TableItem {...tableStyles}>...</TableItem>
              </TableRow>
            </TableBody>
          </Table>
        </div>

        <div style={{ marginLeft: "-4rem", marginTop: "4rem" }}></div>

        <Heading size={6} textColor="quartenary">
          Command
        </Heading>

        <Layout>
          <Fill margin={5}>
            <button
              type="button"
              {...buttonStyles}
              onClick={this.createSimpleDatabaseRecord}
            >
              Create Ticket
            </button>
          </Fill>
          <Fill>
            <button
              type="button"
              {...buttonStyles}
              onClick={this.updateSimpleDatabaseRecord}
            >
              Update Ticket
            </button>
          </Fill>
          <Fill>
            <button
              type="button"
              {...buttonStyles}
              onClick={this.deleteSimpleDatabaseRecord}
            >
              Delete Ticket
            </button>
          </Fill>
        </Layout>
      </div>
    );
  }
}

class EventDatabaseExample extends React.Component {
  constructor(props) {
    super(props);
    this.initialState = {
      eventsDatabase: {
        updateIndex: 0,
        highlighted: [],
        rows: []
      }
    };
    this.state = this.initialState;
  }

  createEventsRecord = () => {
    this.setState({
      eventsDatabase: {
        updateIndex: 0,
        highlighted: [],
        rows: [
          {
            id: "7",
            type: "Ticket.Created",
            data: {
              name: "1st name",
              description: "1st description",
              timestamp: "..."
            }
          }
        ]
      }
    });
  };

  updateEventsRecord = () => {
    const updateIndex = this.state.eventsDatabase.updateIndex;
    const newEvents = [...this.state.eventsDatabase.rows];

    switch (updateIndex) {
      case 0:
        newEvents.push({
          id: "7",
          type: "Ticket.Updated",
          data: {
            name: "2nd name",
            timestamp: "..."
          }
        });
        break;
      case 1:
        newEvents.push({
          id: "7",
          type: "Ticket.Updated",
          data: {
            name: "3rd name",
            timestamp: "..."
          }
        });
        break;
      case 2:
        newEvents.push({
          id: "7",
          type: "Ticket.Updated",
          data: {
            name: "4th name",
            description: "3rd name",
            timestamp: "..."
          }
        });
        break;
    }

    this.setState({
      eventsDatabase: {
        updateIndex: updateIndex + 1,
        highlighted: [],
        rows: newEvents
      }
    });
  };

  deleteEventsRecord = () => {
    const updateIndex = this.state.eventsDatabase.updateIndex;
    const newEvents = [...this.state.eventsDatabase.rows];
    newEvents.push({
      id: "7",
      type: "Ticket.Deleted",
      data: {
        timestamp: "..."
      }
    });

    this.setState({
      eventsDatabase: {
        updateIndex: updateIndex + 1,
        rows: newEvents
      }
    });
  };

  render() {
    return (
      <div>
        <Heading size={4} textColor="tertiary">
          Events Table
        </Heading>

        <div style={{ marginLeft: "-15rem", marginTop: "4rem" }}>
          <Table {...tableStyles}>
            <TableHeader>
              <TableRow>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 0.7rem" }}>id</div>
                </TableHeaderItem>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 5rem" }}>type</div>
                </TableHeaderItem>
                <TableHeaderItem {...tableStyles}>
                  <div style={{ margin: "0 30rem" }}>data</div>
                </TableHeaderItem>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow {...tableStyles}>
                <TableItem {...tableStyles}>
                  <Text style={{ fontSize: "1rem" }}>...</Text>
                </TableItem>
                <TableItem {...tableStyles}>
                  <Text style={{ fontSize: "1rem" }}>...</Text>
                </TableItem>
                <TableItem {...tableStyles}>
                  <Text style={{ fontSize: "1rem" }}>...</Text>
                </TableItem>
              </TableRow>
              {this.state.eventsDatabase.rows.map((row, id) => {
                const itemStyles = name => {
                  const isData = name === "data";
                  const isLastRow =
                    id + 1 === this.state.eventsDatabase.rows.length;
                  return {
                    ...tableStyles,
                    style: {
                      ...tableStyles.style,
                      fontSize: isData ? "1.5rem" : "inherit",
                      backgroundColor: isLastRow
                        ? tableHighlightBackgroundColor
                        : "inherit"
                    }
                  };
                };

                return (
                  <TableRow key={id}>
                    <TableItem {...itemStyles("id")}>
                      <div style={{ margin: "0.3rem", textAlign: "left" }}>
                        {row.id}
                      </div>
                    </TableItem>
                    <TableItem {...itemStyles("type")}>
                      <div style={{ margin: "0.3rem", textAlign: "left" }}>
                        {row.type}
                      </div>
                    </TableItem>
                    <TableItem {...itemStyles("data")}>
                      <pre style={{ textAlign: "left" }}>
                        {JSON.stringify(row.data)}
                      </pre>
                    </TableItem>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </div>

        <div style={{ marginLeft: "-4rem", marginTop: "4rem" }}></div>

        <Layout>
          <Fill margin={5}>
            <button
              type="button"
              {...buttonStyles}
              onClick={this.createEventsRecord}
            >
              Create Ticket
            </button>
          </Fill>
          <Fill>
            <button
              type="button"
              {...buttonStyles}
              onClick={this.updateEventsRecord}
            >
              Update Ticket
            </button>
          </Fill>
          <Fill>
            <button
              type="button"
              {...buttonStyles}
              onClick={this.deleteEventsRecord}
            >
              Delete Ticket
            </button>
          </Fill>
        </Layout>
      </div>
    );
  }
}

export default WithSlidesLink(
  class Presentation extends React.Component {
    render() {
      return (
        <Deck
          transition={["zoom", "slide"]}
          theme={theme}
          transitionDuration={500}
          onStateChange={this.resetState}
        >
          <Slide transition={["zoom"]} bgColor="primary">
            <Heading size={1} caps lineHeight={1} textColor="tertiary">
              Event Sourcing
            </Heading>
            <Heading size={4} caps lineHeight={1} textColor="quartenary">
              The crash course
            </Heading>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Ticket management system
            </Heading>

            <List>
              <ListItem textColor="primary">Create Tickets</ListItem>
              <ListItem textColor="primary">Update Tickets</ListItem>
              <ListItem textColor="primary">Delete Tickets</ListItem>
              <ListItem textColor="primary">List Tickets</ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Typical approach...
            </Heading>
            <List>
              <ListItem textColor="primary">
                Simple database - one row per ticket
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="primary">
            <SimpleDatabaseExample />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Getting tickets...
            </Heading>
            <List>
              <ListItem textColor="primary">Active Record Pattern</ListItem>
              <ListItem textColor="primary">
                ORM - Object-relational mapping
              </ListItem>
              <ListItem textColor="primary">
                select * from tickets where id = id
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Event sourcing approach...
            </Heading>
            <List>
              <ListItem textColor="primary">A command triggers events</ListItem>
              <ListItem textColor="primary">
                An event describes something that has happened in the past
              </ListItem>
              <ListItem textColor="primary">
                Each event has an entity id, event type, and relevant data
              </ListItem>
              <ListItem textColor="primary">
                We could store each event in a database row
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="primary" align="flex-start">
            <EventDatabaseExample />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Events to entities
            </Heading>
            <List>
              <ListItem textColor="primary">
                Stream the events, compute state
              </ListItem>
            </List>
          </Slide>

          <Slide
            transition={["slide"]}
            bgColor="secondary"
            style={{ overflow: "scroll" }}
          >
            <Heading size={4} textColor="tertiary">
              (Naive) Getting tickets...
            </Heading>
            <CodePane
              lang="python"
              source={require("raw-loader!../assets/computing-state.example")}
              margin="20px auto"
              style={{ fontSize: "2rem" }}
            />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Done. Ship it.
            </Heading>
            <Heading size={1} textColor="tertiary">
              🚢
            </Heading>
          </Slide>

          <Slide
            transition={["slide"]}
            bgColor="secondary"
            style={{ overflow: "scroll" }}
          >
            <Heading size={4} textColor="tertiary">
              johnbywater/eventsourcing
            </Heading>
            <CodePane
              lang="python"
              style={{ fontSize: "1.5rem" }}
              source={`
from eventsourcing.domain.model.aggregate import AggregateRoot

class Ticket(AggregateRoot):
  def __init__(
      self, name: Optional[str] = None, description: Optional[str] = None, **kwargs
  ):
      super(Ticket, self).__init__(**kwargs)
      self.name = name
      self.description = description

    # command handler
    def rename(self, name: str):
      self.__trigger_event__(Ticket.Renamed, name=name)

    # Listens to an event, and causes the mutation on the model
    class Renamed(Event):
      @property
      def name(self) -> str:
          return self.__dict__["name"]

      def mutate(self, ticket: "Ticket"):
          ticket.name = self.name    
`.trim()}
              margin="20px auto"
            />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Expanding our knowledge...
            </Heading>

            <List>
              <ListItem textColor="primary">Commands</ListItem>
              <ListItem textColor="primary">Queries</ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Commands
            </Heading>

            <List>
              <ListItem textColor="primary">Clients send commands</ListItem>
              <ListItem textColor="primary">Commands represent intent</ListItem>
              <ListItem textColor="primary">
                Command handlers: validate + trigger events
              </ListItem>
              <ListItem textColor="primary">
                Naming convention: Verb + Type
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Example command names
            </Heading>
            <List>
              <ListItem textColor="primary">CreateTicket</ListItem>
              <ListItem textColor="primary">ConfirmOrder</ListItem>
              <ListItem textColor="primary">AddAttachment</ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Events
            </Heading>

            <List>
              <ListItem textColor="primary">
                An event describes something that has happened in the past
              </ListItem>
              <ListItem textColor="primary">
                Created by command handlers
              </ListItem>
              <ListItem textColor="primary">
                Naming convention: Type + past-particle Verb
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Example event names
            </Heading>
            <List>
              <ListItem textColor="primary">TicketCreated</ListItem>
              <ListItem textColor="primary">OrderConfirmed</ListItem>
              <ListItem textColor="primary">AttachmentAdded</ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Command -> Event
            </Heading>
            <List>
              <ListItem textColor="primary">
                CreateTicket -> TicketCreated
              </ListItem>
              <ListItem textColor="primary">
                ConfirmOrder -> OrderConfirmed
              </ListItem>
              <ListItem textColor="primary">
                AddAttachment -> AttachmentAdded
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              How to name commands/events?
            </Heading>

            <List>
              <ListItem textColor="primary">
                Use the terminology in your domain
              </ListItem>
              <ListItem textColor="primary">
                Work with domain experts - event storming
              </ListItem>
              <ListItem textColor="primary">
                Define and use your ubiquitous language
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Commands Overview
            </Heading>
            <Image width="100%" src={images.commandArchitecture} />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Projection
            </Heading>
            <Image width="100%" src={images.projection} />
            <Appear>
              <Heading size={6} textColor="quartenary">
                Stream computed state into Elasticsearch, MongoDB, postgres,
                whatever!
              </Heading>
            </Appear>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Queries Overview
            </Heading>
            <Image width="100%" src={images.queryArchitecture} />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Command, Query Responsibility segregation
            </Heading>

            <Heading size={8} textColor="primary" marginTop={10}>
              Separate command and query models
            </Heading>

            <Appear>
              <Heading size={4} textColor="primary">
                CQRS
              </Heading>
            </Appear>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              GraphQL
            </Heading>
          </Slide>

          <Slide
            transition={["slide"]}
            bgColor="secondary"
            style={{ overflow: "scroll" }}
          >
            <Heading size={4} textColor="tertiary">
              Command (Mutation) Types
            </Heading>
            <CodePane
              lang="graphql"
              style={{ fontSize: "2rem" }}
              source={`
mutation ($id: ID!, $name: String!) {
  renameTicket(id: $id, name: $name) {
      ok
  }
}
`.trim()}
              margin="20px auto"
            />
          </Slide>

          <Slide
            transition={["slide"]}
            bgColor="secondary"
            style={{ overflow: "scroll" }}
          >
            <Heading size={4} textColor="tertiary">
              Query Types
            </Heading>
            <CodePane
              lang="graphql"
              style={{ fontSize: "2rem" }}
              source={`
query {
  tickets {
      name
      description
      updatedAt
  }
}
`.trim()}
              margin="20px auto"
            />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Why event sourcing?
            </Heading>
            <List>
              <ListItem textColor="primary">
                Full audit trail - Data mining, bug hunting, admin tools
              </ListItem>
              <ListItem textColor="primary">
                Create new models from existing events
              </ListItem>
              <ListItem textColor="primary">
                Fix bugs in your domain layer
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Why event sourcing?
            </Heading>
            <List>
              <ListItem textColor="primary">
                Add features after the fact
              </ListItem>
              <ListItem textColor="primary">
                Provide users with audit trails/history functionality easily
              </ListItem>
              <ListItem textColor="primary">
                "Scalable" - Append-only datastores are fast
              </ListItem>
              <ListItem textColor="primary">
                It's now "easy" to choose the best datastore for your queries
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Why not event sourcing?
            </Heading>
            <List>
              <ListItem textColor="primary">
                Projections can carry extra overhead
              </ListItem>
              <ListItem textColor="primary">
                Eventual consistency, delays between commands/queries
              </ListItem>
              <ListItem textColor="primary">Event versioning?</ListItem>
              <ListItem textColor="primary">GDPR?</ListItem>
              <ListItem textColor="primary">
                Good for specific use cases
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Hey; What's this DDD thing about?
            </Heading>
            <List>
              <ListItem textColor="primary">Domain Driven Design</ListItem>
              <ListItem textColor="primary">
                Focus on the core domain and domain logic
              </ListItem>
              <ListItem textColor="primary">
                Actively interact with domain experts to define terminology and
                concepts
              </ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Image width="50%" src={images.distilled} />
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Strategical
            </Heading>
            <List>
              <ListItem textColor="primary">Domain</ListItem>
              <ListItem textColor="primary">Domain experts</ListItem>
              <ListItem textColor="primary">Ubiquitous language</ListItem>
              <ListItem textColor="primary">Event storming</ListItem>
              <ListItem textColor="primary">Bounded contexts</ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={4} textColor="tertiary">
              Tactical
            </Heading>
            <List>
              <ListItem textColor="primary">Entities</ListItem>
              <ListItem textColor="primary">Value Objects</ListItem>
              <ListItem textColor="primary">Aggregate Roots</ListItem>
              <ListItem textColor="primary">Event sourcing</ListItem>
              <ListItem textColor="primary">etc</ListItem>
            </List>
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={6} textColor="tertiary">
              github.com/alanfoster
            </Heading>

            <Appear>
              <Heading size={6} textColor="primary" marginTop={5}>
                ticket-management-graphql-eventsourcing
              </Heading>
            </Appear>  
          </Slide>

          <Slide transition={["slide"]} bgColor="secondary">
            <List>
              <ListItem textColor="tertiary">
                johnbywater/eventsourcing
              </ListItem>
              <ListItem textColor="tertiary">
                GraphQL - Graphene
              </ListItem>  
              <ListItem textColor="tertiary">
                 React + Apollo
              </ListItem>                                              
            </List>
          </Slide>          

          <Slide transition={["slide"]} bgColor="secondary">
            <Heading size={1} caps lineHeight={1} textColor="tertiary">
              le fin
            </Heading>
          </Slide>
        </Deck>
      );
    }
  }
);
