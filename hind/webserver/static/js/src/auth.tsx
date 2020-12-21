import * as React from "react";
import * as ReactDOM from "react-dom";

import Card from "./components/Card";
import APIService from "./APIService";

type activeMode = "login" | "signup";

export type AuthModalProps = {
  activeMode: activeMode;
};

type AuthModalState = {
  activeMode: activeMode;
};

export default class AuthModal extends React.Component<
  AuthModalProps,
  AuthModalState
> {
  APIService: APIService;

  constructor(props: AuthModalProps) {
    super(props);
    this.APIService = new APIService(`${window.location.origin}`);

    this.state = {
      activeMode: props.activeMode,
    };
  }

  updateMode = (activeMode: activeMode) => {
    this.setState({ activeMode });
    window.history.pushState(null, "", `/${activeMode}`);
  };

  render() {
    const { activeMode } = this.state;
    return (
      <Card className="auth-card">
        {activeMode === "login" ? (
          <>
            <h4>Hey! Welcome back</h4>
            <form action="/login" method="POST">
              <div className="mb-3">
                <label htmlFor="user_name" className="form-label">
                  User Name
                </label>
                <input
                  type="text"
                  className="form-control"
                  aria-describedby="emailHelp"
                  name="user_name"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="password" className="form-label">
                  Password
                </label>
                <input
                  type="password"
                  className="form-control"
                  name="password"
                  required
                />
              </div>

              <button type="submit" className="btn btn-primary btn-block">
                Log In
              </button>
            </form>
            <div className="mt-3 form-text">
              Do not have an account?
              <button
                type="button"
                className="btn btn-inline"
                onClick={() => {
                  this.updateMode("signup");
                }}
              >
                Sign up
              </button>
            </div>
          </>
        ) : (
          <>
            <h4>Lets get you started</h4>
            <form action="/signup" method="POST">
              <div className="mb-3">
                <label htmlFor="name" className="form-label">
                  Name
                </label>
                <input
                  type="text"
                  className="form-control"
                  aria-describedby="emailHelp"
                  name="name"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="user_name" className="form-label">
                  User Name
                </label>
                <input
                  type="text"
                  className="form-control"
                  aria-describedby="emailHelp"
                  name="user_name"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="user_name" className="form-label">
                  Email ID
                </label>
                <input
                  type="text"
                  className="form-control"
                  aria-describedby="emailHelp"
                  name="email_id  "
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="password" className="form-label">
                  Password
                </label>
                <input
                  type="password"
                  className="form-control"
                  name="password"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="address" className="form-label">
                  Address
                </label>
                <input type="text" className="form-control" name="address" />
              </div>
              <div className="mb-3">
                <label htmlFor="about" className="form-label">
                  About Me
                </label>
                <textarea className="form-control" name="about" />
              </div>

              <button type="submit" className="btn btn-primary btn-block">
                Sign Up
              </button>
            </form>
            <div className="mt-3 form-text">
              Already have an account?
              <button
                type="button"
                className="btn btn-inline"
                onClick={() => {
                  this.updateMode("login");
                }}
              >
                Log in
              </button>
            </div>
          </>
        )}
      </Card>
    );
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(
    <AuthModal activeMode={reactProps.active_mode} />,
    domContainer
  );
});
