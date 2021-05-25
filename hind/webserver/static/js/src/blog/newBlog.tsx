import * as React from "react";
import * as ReactDOM from "react-dom";

import APIService from "../APIService";

export type NewBlogProps = {};

type NewBlogState = {};

export default class NewBlog extends React.Component<
  NewBlogProps,
  NewBlogState
> {
  APIService: APIService;

  constructor(props: NewBlogProps) {
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
        <h4>Create a new Blog</h4>
        <form action="/blog/new" method="POST">
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
            <label htmlFor="location" className="form-label">
              Location
            </label>
            <input type="text" className="form-control" name="location" />
          </div>
          <div className="mb-3">
            <label htmlFor="about" className="form-label">
              Blog Body
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
  ReactDOM.render(<NewBlog />, domContainer);
});
