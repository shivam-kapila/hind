import * as React from "react";
import * as ReactDOM from "react-dom";
import AuthModal from "./auth";

const Landing = () => {
  return (
    <>
      <div className="landing">
        <h1 className="brand">hind</h1>
        <p>Get a glimpse of Hindustani culture and tradition</p>
        <form className="form-inline" action="/search" method="GET">
          <input
            type="text"
            placeholder="Type here to search..."
            name="keyword"
          />
          <button type="submit">&rarr;</button>
        </form>
        <img
          src="/static/img/pattern.svg"
          height="1000"
          className="img-responsive"
          alt=""
        />
      </div>
    </>
  );
};

document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  ReactDOM.render(<Landing />, domContainer);
});
