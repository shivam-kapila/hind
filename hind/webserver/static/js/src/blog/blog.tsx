import * as React from "react";
import * as ReactDOM from "react-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart, faMapMarkerAlt } from "@fortawesome/free-solid-svg-icons";

const MAX_ABOUT_LENGTH = 100;

type BlogProps = {
  blog: any;
};

const Blog = (props: BlogProps) => {
  const { blog } = props;
  return (
    <div className="container">
      <div className="blog row">
        <div className="col-2">
          <div>
            <img
              src={blog.profile_picture_url}
              alt=""
              className="img-fluid profile-picture"
            />
            <p className="mt-3">
              <a href={`/user/${blog.user_name}`}>{blog.user_name}</a>
              <br />
              <span className="text-muted">{blog.name}</span>
            </p>
          </div>
          <p className="small">
            {blog.about && (
              <> {blog.about.substring(0, MAX_ABOUT_LENGTH)} ... </>
            )}
          </p>
          <a
            href={`/user/${blog.user_name}`}
            className="btn btn-sm btn-primary"
          >
            View Profile
          </a>

          <hr className="mt-4 mb-4" />
          <span className="text-muted">
            <FontAwesomeIcon icon={faHeart} /> {blog.like}
          </span>
        </div>
        <div className="col-10 offset-2">
          <h1>{blog.title}</h1>
          <div className="mt-5">
            <img src={blog.upload_res_url} alt="blog cover" height="500px" />
          </div>
          <div className="mt-5 mb-3">
            {blog.tags.map((tag: string) => (
              <span className="badge badge-pill pill secondary" key={tag}>
                {tag}
              </span>
            ))}
          </div>
          <span className="badge badge-pill pill">
            <FontAwesomeIcon icon={faMapMarkerAlt} /> {blog.location}
          </span>
          <p className="mt-5">{blog.body}</p>
        </div>
      </div>
    </div>
  );
};
document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(<Blog blog={reactProps.blog} />, domContainer);
});
