import * as React from "react";
import * as ReactDOM from "react-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart, faMapMarkerAlt } from "@fortawesome/free-solid-svg-icons";

const MAX_ABOUT_LENGTH = 100;

type ProductProps = {
  product: any;
  currentUser: any;
};
type ProductState = {
  bids: [];
};

export default class Product extends React.Component<
  ProductProps,
  ProductState
> {
  constructor(props: ProductProps) {
    super(props);
    this.state = {
      bids: [],
    };
  }

  render() {
    const { product } = this.props;
    const { bids } = this.state;
    return (
      <div className="container">
        <div className="product row">
          <div className="col-2">
            <div>
              <img
                src={product.profile_picture_url}
                alt=""
                className="img-fluid profile-picture"
              />
              <p className="mt-3">
                <a href={`/user/${product.user_name}`}>{product.user_name}</a>
                <br />
                <span className="text-muted">{product.name}</span>
              </p>
            </div>
            <p className="small">
              {product.about && (
                <> {product.about.substring(0, MAX_ABOUT_LENGTH)} ... </>
              )}
              {bids}
            </p>
            <a
              href={`/user/${product.user_name}`}
              className="btn btn-sm btn-primary"
            >
              View Profile
            </a>
          </div>
          <div className="col-md-5 offset-2">
            <h1>{product.title}</h1>
            <div className="mt-5">
              <img
                src={product.upload_res_url}
                alt="product cover"
                height="500px"
              />
            </div>
            <div className="mt-5 mb-3">
              {product.tags.map((tag: string) => (
                <span className="badge badge-pill pill secondary" key={tag}>
                  {tag}
                </span>
              ))}
            </div>
            <span className="badge badge-pill pill">
              <FontAwesomeIcon icon={faMapMarkerAlt} />{" "}
              {product.origin_location}
            </span>
            <p className="mt-5">{product.details}</p>
          </div>
          <div className="col-md-5">
            <h4 className="text-muted">Previous Bids</h4>
            {product.bids.map((bid: any) => (
              <div>{bid.id}</div>
            ))}
          </div>
        </div>
      </div>
    );
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const domContainer = document.querySelector("#react-container");
  const propsElement = document.getElementById("react-props");
  const reactProps = JSON.parse(propsElement!.innerHTML);
  ReactDOM.render(
    <Product
      product={reactProps.product}
      currentUser={reactProps.current_user}
    />,
    domContainer
  );
});
