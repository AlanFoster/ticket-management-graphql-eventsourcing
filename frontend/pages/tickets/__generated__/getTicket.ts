/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: getTicket
// ====================================================

export interface getTicket_ticket_history {
  __typename: "HistoryItem";
  field: string;
  oldValue: string | null;
  newValue: string | null;
  timestamp: any;
}

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
