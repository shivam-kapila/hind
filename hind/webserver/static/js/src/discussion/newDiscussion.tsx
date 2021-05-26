import * as React from "react";
import * as ReactDOM from "react-dom";

import APIService from "../APIService";

export type NewDiscussionProps = {};

type NewDiscussionState = {};

export default class NewDiscussion extends React.Component<
  NewDiscussionProps,
  NewDiscussionState
> {
  APIService: APIService;

  constructor(props: NewDiscussionProps) {
    super(props);
    this.APIService = new APIService(`${window.location.origin}`);
  }

  //   updateMode = (activeMode: activeMode) => {
  //     this.setState({ activeMode });
  //     window.history.pushState(null, "", `/${activeMode}`);
  //   };

  render() {
    return (
      <div>
        <h4>Create a new Discussion</h4>
        <form action="/discussions/new" method="POST">
          <div className="mb-3">
            <label htmlFor="title" className="form-label">
              Title
            </label>
            <input type="text" className="form-control" name="title" required />
          </div>
          <div className="mb-3">
            <label htmlFor="tags" className="form-label">
              Tags
            </label>
            <input type="text" className="form-control" name="tags" required />
          </div>
          <div className="mb-3">
            <label htmlFor="about" className="form-label">
              Discussion Body
            </label>
            <textarea className="form-control" name="body" rows={40} />
          </div>

          <button type="submit" className="btn btn-primary btn-block">
            Create
          </button>
        </form>
      </div>
    );
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  //   const propsElement = document.getElementById("react-props");
  //   const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(<NewDiscussion />, domContainer);
});
