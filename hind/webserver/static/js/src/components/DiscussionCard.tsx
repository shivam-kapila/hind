import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import * as React from "react";
import Card from "./Card";

const MAX_DISCUSSION_BODY_LENGTH = 100;

type pageTypes = "search" | "user";

type discussionCardProps = {
  discussion: any;
  pageType?: pageTypes;
};

const DiscussionCard = (props: discussionCardProps) => {
  const { discussion, pageType } = props;
  return (
    <Card className="col-md-8 discussion-card">
      <div className="row">
        <div className="col-12">
          <div>
            <h4>{discussion.title}</h4>
            <p className="text-muted">
              {discussion.body.substring(0, MAX_DISCUSSION_BODY_LENGTH)}...
            </p>
          </div>
          <div className="row mt-auto">
            <div className="col-10">
              {pageType === "search" ? (
                <>
                  <img
                    src={discussion.profile_picture_url}
                    alt=""
                    className="img-fluid profile-picture"
                  />
                  <p className="mt-3">
                    {discussion.user_name}
                    <br />
                    <span className="text-muted">{discussion.name}</span>
                  </p>
                </>
              ) : (
                <span className="badge badge-pill pill mt-4">
                  {discussion.category}
                </span>
              )}
            </div>
            <div className="col-2">
              <a
                type="submit"
                className="circular-button mt-3"
                href={`/discussions/${discussion.id}`}
              >
                <FontAwesomeIcon icon={faArrowRight} />
              </a>
            </div>
          </div>
        </div>
      </div>
    </Card>
  );
};

DiscussionCard.defaultProps = {
  pageType: "search",
};
export default DiscussionCard;
