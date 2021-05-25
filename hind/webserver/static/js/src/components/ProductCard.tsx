import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import * as React from "react";
import Card from "./Card";

const MAX_BLOG_BODY_LENGTH = 100;

type page = "search" | "user";

type productCardProps = {
  product: any;
  pageType?: page;
};

const ProductCard = (props: productCardProps) => {
  const { product, pageType } = props;
  return (
    <Card className="col-md-4 product-card">
      <div className="row">
        <div className="col-12">
          <img src={product.upload_res_url} alt="" className="img-fluid" />
        </div>
        <div className="col-12">
          <div>
            <h4>{product.name}</h4>
            <p className="text-muted">
              {product.description.substring(0, MAX_BLOG_BODY_LENGTH)}...
            </p>
          </div>
          <div className="row mt-auto">
            <div className="col-10">
              {pageType === "search" ? (
                <>
                  <img
                    src={product.profile_picture_url}
                    alt=""
                    className="img-fluid profile-picture"
                  />
                  <p className="mt-3">
                    {product.user_name}
                    <br />
                    <span className="text-muted">{product.name}</span>
                  </p>
                </>
              ) : (
                <span className="badge badge-pill pill mt-4">
                  {product.category}
                </span>
              )}
            </div>
            <div className="col-2">
              <a
                type="submit"
                className="circular-button mt-3"
                href={`/product/${product.id}`}
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

ProductCard.defaultProps = {
  pageType: "search",
};
export default ProductCard;
