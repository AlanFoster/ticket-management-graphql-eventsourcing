/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: getTicket
// ====================================================

export interface getTicket_ticket {
  __typename: "Ticket";
  id: string;
  name: string | null;
  description: string | null;
  updatedAt: any;
}

export interface getTicket {
  ticket: getTicket_ticket | null;
}

export interface getTicketVariables {
  id: string;
}
