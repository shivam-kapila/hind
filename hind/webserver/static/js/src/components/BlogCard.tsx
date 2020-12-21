import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import * as React from "react";
import Card from "./Card";

const MAX_BLOG_BODY_LENGTH = 100;

type pageType = "search" | "user";

type blogCardProps = {
  blog: any;
  pageType?: pageType;
};

const BlogCard = (props: blogCardProps) => {
  const { blog, pageType } = props;
  return (
    <Card className="col-md-8 blog-card">
      <div className="row">
        <div className="col-4">
          <img src={blog.upload_res_url} alt="" className="img-fluid" />
        </div>
        <div className="col-8">
          <div>
            <h4>{blog.title}</h4>
            <p className="text-muted">
              {blog.body.substring(0, MAX_BLOG_BODY_LENGTH)}...
            </p>
          </div>
          <div className="row mt-auto">
            <div className="col-10">
              {pageType === "search" ? (
                <>
                  <img
                    src={blog.profile_picture_url}
                    alt=""
                    className="img-fluid profile-picture"
                  />
                  <p className="mt-3">
                    {blog.user_name}
                    <br />
                    <span className="text-muted">{blog.name}</span>
                  </p>
                </>
              ) : (
                <span className="badge badge-pill pill mt-4">
                  {blog.category}
                </span>
              )}
            </div>
            <div className="col-2">
              <a
                type="submit"
                className="circular-button mt-3"
                href={`blog/${blog.id}`}
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

BlogCard.defaultProps = {
  pageType: "search",
};
export default BlogCard;
