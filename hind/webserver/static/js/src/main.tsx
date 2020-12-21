import * as React from "react";
import * as ReactDOM from "react-dom";

import Card from "./components/Card";
import APIService from "./APIService";

type activeMode = "login" | "signup";

type AuthModalProps = {
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

  render() {
    const { activeMode } = this.state;
    return (
      <Card>
        {activeMode === "login" ? <h1>Hey</h1> : <h1>Lets get you started</h1>}
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
