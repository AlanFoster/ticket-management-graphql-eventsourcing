/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: renameTicket
// ====================================================

export interface renameTicket_renameTicket {
  __typename: "RenameTicket";
  ok: boolean;
}

export interface renameTicket {
  renameTicket: renameTicket_renameTicket | null;
}

export interface renameTicketVariables {
  id: string;
  name: string;
}
