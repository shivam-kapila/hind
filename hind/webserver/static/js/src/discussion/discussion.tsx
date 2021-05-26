import * as timeago from "time-ago";
import * as React from "react";
import * as ReactDOM from "react-dom";

const MAX_ABOUT_LENGTH = 100;

type DiscussionProps = {
  discussion: any;
};

const Discussion = (props: DiscussionProps) => {
  const { discussion } = props;
  return (
    <div className="container">
      <div className="discussion row">
        <div className="col-2">
          <div>
            <img
              src={discussion.profile_picture_url}
              alt=""
              className="img-fluid profile-picture"
            />
            <p className="mt-3">
              <a href={`/user/${discussion.user_name}`}>
                {discussion.user_name}
              </a>
              <br />
              <span className="text-muted">{discussion.name}</span>
            </p>
          </div>
          <p className="small">
            {discussion.about && (
              <> {discussion.about.substring(0, MAX_ABOUT_LENGTH)} ... </>
            )}
          </p>
          <a
            href={`/user/${discussion.user_name}`}
            className="btn btn-sm btn-primary"
          >
            View Profile
          </a>
        </div>
        <div className="col-10 offset-2">
          <h1>{discussion.title}</h1>
          <p className="mt-1">{discussion.body}</p>
          <div className="mt-2 mb-5">
            {discussion.tags.map((tag: string) => (
              <span className="badge badge-pill pill secondary" key={tag}>
                {tag}
              </span>
            ))}
          </div>
          <h5 className="text-center text-muted">COMMENTS</h5>
          <hr />
          <form action={`/discussions/${discussion.id}/comment`} method="post">
            <input
              type="text"
              placeholder="Add a comment"
              name="body"
              defaultValue=""
            />
            <button type="submit" className="btn btn-sm btn-primary">
              Comment
            </button>
          </form>
          {discussion.comments.map((comment: any) => (
            <div className="mt-2" key={comment.id}>
              <div className="comment">
                <i>
                  <small className="text-muted float-end">
                    {new Date(comment.created * 1000).toLocaleString(
                      undefined,
                      {
                        day: "2-digit",
                        month: "short",
                        hour: "numeric",
                        minute: "numeric",
                        hour12: true,
                      }
                    )}
                  </small>
                </i>
                <b>
                  <p className="bold">{comment.name}</p>
                </b>
                {comment.body}
                <div className="col-11 offset-1">
                  <form
                    action={`/discussions/${discussion.id}/comment/${comment.id}/comment`}
                    method="post"
                  >
                    <input
                      type="text"
                      placeholder="Add a sub comment"
                      name="body"
                      defaultValue=""
                    />
                    <button type="submit" className="btn btn-sm btn-primary">
                      Comment
                    </button>
                  </form>
                  {comment.sub_comments.map((subComment: any) => (
                    <div className="mt-5" key={subComment.id}>
                      <i>
                        <small className="text-muted float-end">
                          {new Date(subComment.created * 1000).toLocaleString(
                            undefined,
                            {
                              day: "2-digit",
                              month: "short",
                              hour: "numeric",
                              minute: "numeric",
                              hour12: true,
                            }
                          )}
                        </small>
                      </i>
                      <b>
                        <p className="bold">{subComment.name}</p>
                      </b>
                      {subComment.body}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(
    <Discussion discussion={reactProps.discussion} />,
    domContainer
  );
});
