import * as React from "react";
import * as ReactDOM from "react-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMapMarkerAlt } from "@fortawesome/free-solid-svg-icons";

type profileProps = {
  currentUser: any;
};

const Profile = (props: profileProps) => {
  const { currentUser } = props;
  return (
    <div className="profile">
      <h2>
        {currentUser.name} ({currentUser.user_name})
      </h2>
      <span className="badge badge-pill pill">
        <FontAwesomeIcon icon={faMapMarkerAlt} /> {currentUser.address}
      </span>
      <p className="text-muted">{currentUser.about}</p>

      <div className="blogs" />
    </div>
  );
};
document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(
    <Profile currentUser={reactProps.current_user} />,
    domContainer
  );
});
