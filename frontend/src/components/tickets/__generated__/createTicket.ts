/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: createTicket
// ====================================================

export interface createTicket_createTicket_ticket {
  __typename: "Ticket";
  id: string;
  name: string | null;
  updatedAt: any;
}

export interface createTicket_createTicket {
  __typename: "CreateTicket";
  ok: boolean;
  ticket: createTicket_createTicket_ticket;
}

export interface createTicket {
  createTicket: createTicket_createTicket | null;
}

export interface createTicketVariables {
  name: string;
  description: string;
}
