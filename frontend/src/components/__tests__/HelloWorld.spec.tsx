import * as React from "react";
import renderer from "react-test-renderer";

const SimpleComponent = () => <div>hello world</div>

describe("Link", function () {
    it("renders successfully", function () {
        const tree = renderer.create(<SimpleComponent />);

        expect(tree).toMatchSnapshot();
    });
});
