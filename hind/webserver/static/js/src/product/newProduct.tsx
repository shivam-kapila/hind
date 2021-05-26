import * as React from "react";
import * as ReactDOM from "react-dom";

import APIService from "../APIService";

export type NewProductProps = {};

type NewProductState = {};

export default class NewProduct extends React.Component<
  NewProductProps,
  NewProductState
> {
  APIService: APIService;

  constructor(props: NewProductProps) {
    super(props);
    this.APIService = new APIService(`${window.location.origin}`);
  }

  render() {
    return (
      <div>
        <h4>Add a new Product</h4>
        <form action="/products/new" method="POST">
          <div className="mb-3">
            <label htmlFor="name" className="form-label">
              Title
            </label>
            <input type="text" className="form-control" name="name" required />
          </div>
          <div className="mb-3">
            <label htmlFor="tags" className="form-label">
              Tags
            </label>
            <input type="text" className="form-control" name="tags" required />
          </div>
          <div className="mb-3">
            <label htmlFor="origin_location" className="form-label">
              Origin Location
            </label>
            <input
              type="text"
              className="form-control"
              name="origin_location"
            />
          </div>
          <div className="mb-3">
            <label htmlFor="about" className="form-label">
              Product Description
            </label>
            <textarea className="form-control" name="description" rows={40} />
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
  ReactDOM.render(<NewProduct />, domContainer);
});
