import * as React from "react";
import { render, cleanup } from "@testing-library/react";
import { Placeholder } from "../placeholder";

describe("Placeholder", function() {
    afterEach(cleanup);

    it("works with no count provided", function() {
        const { container } = render(
            <Placeholder />
        );

        expect(container).toMatchSnapshot();
    });

    it("works with a count provided", function() {
        const { container } = render(
            <Placeholder count={3} />
        );

        expect(container).toMatchSnapshot();
    });
});
