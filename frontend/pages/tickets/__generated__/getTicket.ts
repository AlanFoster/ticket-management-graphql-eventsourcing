/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: getTicket
// ====================================================

export interface getTicket_ticket_history_TicketFieldUpdated {
  __typename: "TicketFieldUpdated";
  timestamp: any;
  field: string;
  oldValue: string | null;
  newValue: string | null;
}

export interface getTicket_ticket_history_TicketCloned {
  __typename: "TicketCloned";
  timestamp: any;
  originalTicketId: string | null;
  originalTicketName: string | null;
}

export type getTicket_ticket_history = getTicket_ticket_history_TicketFieldUpdated | getTicket_ticket_history_TicketCloned;

export interface getTicket_ticket {
  __typename: "Ticket";
  id: string;
  name: string | null;
  description: string | null;
  updatedAt: any;
  history: getTicket_ticket_history[];
}

export interface getTicket {
  ticket: getTicket_ticket | null;
}

export interface getTicketVariables {
  id: string;
}
