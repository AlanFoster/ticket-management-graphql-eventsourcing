/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: getTickets
// ====================================================

export interface getTickets_tickets {
  __typename: "Ticket";
  id: string;
  name: string | null;
  updatedAt: any;
}

export interface getTickets {
  tickets: getTickets_tickets[] | null;
}
