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

  // getFollowers = () => {
  //   const { user } = this.props;
  //   this.APIService.getFollowersOfUser(user.name).then(
  //     ({ followers }: { followers: Array<{ musicbrainz_id: string }> }) => {
  //       this.setState({
  //         followerList: followers.map(({ musicbrainz_id }) => {
  //           return {
  //             name: musicbrainz_id,
  //           };
  //         }),
  //       });
  //     }
  //   );
  // };

  // getFollowing = () => {
  //   const { user } = this.props;
  //   this.APIService.getFollowingForUser(user.name).then(
  //     ({ following }: { following: Array<{ musicbrainz_id: string }> }) => {
  //       this.setState({
  //         followingList: following.map(({ musicbrainz_id }) => {
  //           return { name: musicbrainz_id };
  //         }),
  //       });
  //     }
  //   );
  // };

  // updateMode = (mode: "follower" | "following") => {
  //   this.setState({ activeMode: mode }, () => {
  //     const { activeMode } = this.state;
  //     if (activeMode === "follower") this.getFollowers();
  //     else this.getFollowing();
  //   });
  // };

  // loggedInUserFollowsUser = (user: ListenBrainzUser): boolean => {
  //   const { followingList } = this.state;
  //   return _includes(
  //     followingList.map((listEntry: ListenBrainzUser) => listEntry.name),
  //     user.name
  //   );
  // };

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
