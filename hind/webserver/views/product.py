import ujson

import hind.db.product as db_product
from flask import Blueprint, render_template, current_app, request
from flask_login import current_user, login_required
from hind.webserver.views.api_tools import _get_non_negative_param
from hind.db.models.product import Product
from hind.webserver import flash
from flask_login import current_user, login_required

product_bp = Blueprint('products', __name__)


@product_bp.route("/<int:product_id>")
def product(product_id):
    product = db_product.get(id=product_id)
    if not product:
        flash.error("Couldn't find a product with ID: %s" % product_id)
        return render_template(
            "base.html",
        )
    user = {}
    if current_user and current_user.is_authenticated:
        user = dict(current_user)
    props = {
        "product": dict(product),
        "current_user": user,
    }

    return render_template(
        "product/product.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )


@product_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():

    if request.method == "POST":
        name = request.form.get("name")
        # category = request.form.get("user_name")
        origin_location = request.form.get("origin_location")
        current_app.logger.error(origin_location)
        description = request.form.get("description")
        tags = request.form.get("tags")
        current_app.logger.debug(current_user)
        try:
            product_id = db_product.create(Product(
                name=name,
                user_id=current_user.id,
                category="local trivia",
                origin_location=origin_location,
                description=description,
                upload_res_url="https://placeimg.com/152/97/any",
                tags=["food"]
            ))

        except Exception as e:
            flash.error(e)
            return render_template(
                "product/new_product.html",
            )
    return render_template(
        "product/new_product.html",
    )


@product_bp.route("/")
def index():
    limit = _get_non_negative_param("limit", default=5)
    offset = _get_non_negative_param("offset", default=0)

    products = db_product.get_products(limit=limit, offset=offset)
    props = {
        "search_type": "product",
        "current_user": current_user,
        "products": products,
        "limit": limit,
        "offset": offset
    }
    return render_template(
        "index/search.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )
