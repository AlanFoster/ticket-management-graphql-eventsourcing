/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: updateTicketDescription
// ====================================================

export interface updateTicketDescription_updateTicketDescription {
  __typename: "UpdateTicketDescription";
  ok: boolean;
}

export interface updateTicketDescription {
  updateTicketDescription: updateTicketDescription_updateTicketDescription | null;
}

export interface updateTicketDescriptionVariables {
  id: string;
  description: string;
}
