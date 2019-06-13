import React, {useState} from 'react';
import { EditableTextInput } from "../editable-text-input";

export default function Show({ ticket }) {
    const [name, setName] = useState(ticket.name);

    return (
        <React.Fragment>
            <EditableTextInput
                key={name}
                value={name}
                onChange={name => setName(name)}
            />
        </React.Fragment>
    );
}
