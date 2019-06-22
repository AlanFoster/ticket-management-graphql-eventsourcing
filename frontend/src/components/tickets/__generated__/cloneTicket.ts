/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: cloneTicket
// ====================================================

export interface cloneTicket_cloneTicket_ticket {
  __typename: "Ticket";
  id: string;
}

export interface cloneTicket_cloneTicket {
  __typename: "CloneTicket";
  ok: boolean;
  ticket: cloneTicket_cloneTicket_ticket;
}

export interface cloneTicket {
  cloneTicket: cloneTicket_cloneTicket | null;
}

export interface cloneTicketVariables {
  id: string;
}
