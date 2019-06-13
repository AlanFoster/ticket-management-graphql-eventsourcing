import * as React from "react";
import { render, fireEvent, cleanup } from "@testing-library/react";
import { EditableTextInput } from "../editable-text-input";

describe("EditableText", function() {
    afterEach(cleanup);

    it("shows the given initial value", function() {
        const onChange = jest.fn();
        const { container } = render(
            <EditableTextInput value="Initial value" onChange={onChange} />
        );

        expect(onChange).toHaveBeenCalledTimes(0);
        expect(container).toMatchSnapshot();
    });

    it("can be edited", function() {
        const onChange = jest.fn();
        const { getByText, getByDisplayValue, container } = render(
            <EditableTextInput value="Initial value" onChange={onChange} />
        );

        fireEvent.click(getByText(/initial value/i));
        fireEvent.change(getByDisplayValue(/initial value/i), {
            target: { value: "new value" }
        });
        fireEvent.blur(getByDisplayValue(/new value/i));

        expect(onChange).toHaveBeenCalledTimes(1);
        expect(onChange).toHaveBeenCalledWith("new value");
        expect(container).toMatchSnapshot();
    });
});
