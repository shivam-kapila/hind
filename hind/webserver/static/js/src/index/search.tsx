import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import * as React from "react";
import * as ReactDOM from "react-dom";
import BlogCard from "../components/BlogCard";
import DiscussionCard from "../components/DiscussionCard";
import ProductCard from "../components/ProductCard";

type searchProps = {
  keyword: string;
  searchType: string;
  blogs: [];
  products: [];
  discussions: [];
  limit: number;
  offset: number;
};

const Search = (props: searchProps) => {
  const { blogs, products, discussions, limit, offset, searchType, keyword } =
    props;

  let baseURL = `${window.location.protocol}//${
    window.location.host
  }${window.location.pathname.replace(/\/$/, "")}`;
  baseURL += `?`;

  if (keyword) {
    baseURL += `keyword=${keyword}&`;
  }

  if (searchType && window.location.pathname === "/search") {
    baseURL += `keyword=${searchType}&`;
  }

  return (
    <div className="search">
      <form
        className="form-inline text-center mb-5"
        action="/search"
        method="GET"
      >
        <input
          type="text"
          placeholder="Type here to search..."
          name="keyword"
          defaultValue=""
        />
        <input type="text" hidden name="type" value={searchType} />
        <button type="submit" className="circular-button">
          <FontAwesomeIcon icon={faArrowRight} />
        </button>
      </form>
      {(!blogs || !blogs.length) &&
      (!products || !products.length) &&
      (!discussions || !discussions.length) ? (
        <p className="text-center text-muted"> No more results to display </p>
      ) : (
        <>
          {blogs && (
            <>
              <h4 className="text-muted text-center mt-5 mb-2">Blogs</h4>
              <div className="row justify-content-md-center">
                {blogs.map((blog: any) => (
                  <BlogCard blog={blog} key={`${blog.id}`} />
                ))}
              </div>
            </>
          )}
          {products && (
            <>
              <h4 className="text-muted text-center mt-5 mb-2">Products</h4>
              <div className="row justify-content-md-center">
                {products.map((product: any) => (
                  <ProductCard product={product} key={`${product.id}`} />
                ))}
              </div>
            </>
          )}
          {discussions && (
            <>
              <h4 className="text-muted text-center mt-5 mb-2">Discussions</h4>
              <div className="row justify-content-md-center">
                {discussions.map((discussion: any) => (
                  <DiscussionCard
                    discussion={discussion}
                    key={`${discussion.id}`}
                  />
                ))}
              </div>
            </>
          )}{" "}
          <div className="pagination-controls text-center">
            {offset > 0 && (
              <a
                href={`${baseURL}limit=${limit}&offset=${offset - limit}`}
                className="btn-primary"
              >
                Previous
              </a>
            )}
            <a
              href={`${baseURL}limit=${limit}&offset=${limit + offset}`}
              className="btn-primary"
            >
              Next
            </a>
          </div>
        </>
      )}
    </div>
  );
};

document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(
    <Search
      keyword={reactProps.keyword}
      searchType={reactProps.search_type}
      blogs={reactProps.blogs}
      products={reactProps.products}
      discussions={reactProps.discussions}
      limit={reactProps.limit}
      offset={reactProps.offset}
    />,
    domContainer
  );
});
