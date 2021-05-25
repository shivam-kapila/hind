import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import * as React from "react";
import * as ReactDOM from "react-dom";
import BlogCard from "../components/BlogCard";
import ProductCard from "../components/ProductCard";

type productProps = {
  blogs: [];
  products: [];
  limit: number;
  offset: number;
};

const Product = (props: productProps) => {
  const { blogs, products, limit, offset } = props;
  const keyword =
    new URL(window.location.href).searchParams.get("keyword") || undefined;
  return (
    <div className="product">
      <form
        className="form-inline text-center mb-5"
        action="/product/search"
        method="GET"
      >
        <input
          type="text"
          placeholder="Type here to search..."
          name="keyword"
          defaultValue={keyword}
        />
        <button type="submit" className="circular-button">
          <FontAwesomeIcon icon={faArrowRight} />
        </button>
      </form>

      <div className="row justify-content-md-center">
        {blogs.map((blog: any) => (
          <BlogCard blog={blog} key={`${blog.id}`} />
        ))}
      </div>

      <div className="row justify-content-md-center">
        {products.map((product: any) => (
          <ProductCard product={product} key={`${product.id}`} />
        ))}
      </div>

      <div className="pagination-controls text-center">
        <a
          href={`${window.location.href}&limit=${limit}&offset=${
            offset - limit
          }`}
          className="btn-primary"
        >
          Previous
        </a>
        <a
          href={`${window.location.href}&limit=${limit}&offset=${
            limit + offset
          }`}
          className="btn-primary"
        >
          Next
        </a>
      </div>
    </div>
  );
};

document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(
    <Product
      blogs={reactProps.blogs}
      products={reactProps.products}
      limit={reactProps.limit}
      offset={reactProps.offset}
    />,
    domContainer
  );
});
