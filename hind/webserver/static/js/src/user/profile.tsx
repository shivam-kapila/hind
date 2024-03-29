import * as React from "react";
import * as ReactDOM from "react-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMapMarkerAlt } from "@fortawesome/free-solid-svg-icons";
import BlogCard from "../components/BlogCard";
import ProductCard from "../components/ProductCard";

type profileProps = {
  user: any;
  blogs: [];
  products: [];
};

const Profile = (props: profileProps) => {
  const { user, blogs, products } = props;
  return (
    <>
      <div className="profile row mb-5">
        <div className="col-4">
          <img src={user.profile_picture_url} alt="" />
        </div>
        <div className="col-8">
          <h2>{user.name}</h2>
          <h4 className="text-muted mb-2">{user.user_name}</h4>
          <span className="badge badge-pill pill mb-4">
            <FontAwesomeIcon icon={faMapMarkerAlt} /> {user.address}
          </span>
          <p>{user.about}</p>
        </div>
      </div>
      {blogs && (
        <>
          <h4 className="text-muted text-center mt-5 mb-2">
            Some blogs penned down by me
          </h4>
          <div className="row justify-content-md-center">
            {blogs.map((blog: any) => (
              <BlogCard blog={blog} key={`${blog.id}`} />
            ))}
          </div>
        </>
      )}
      {products && (
        <>
          <h4 className="text-muted text-center mt-5 mb-2">
            Some products by me
          </h4>
          <div className="row justify-content-md-center">
            {products.map((product: any) => (
              <ProductCard product={product} key={`${product.id}`} />
            ))}
          </div>
        </>
      )}
    </>
  );
};
document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(
    <Profile
      user={reactProps.user}
      blogs={reactProps.blogs}
      products={reactProps.products}
    />,
    domContainer
  );
});
