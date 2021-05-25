import ujson
import hind.db.blog as db_blog
import hind.db.user as db_user
import hind.db.product as db_product

from hind.webserver import flash
from flask import Blueprint, render_template
from flask_login import current_user, login_required


user_bp = Blueprint('user', __name__)


@user_bp.route("/profile")
@login_required
def profile():
    blogs = db_blog.get_blogs_for_user(user_id=current_user.id, limit=5, offset=0)
    products = db_product.get_products_for_user(user_id=current_user.id, limit=5, offset=0)
    props = {
        "user": dict(current_user),
        "blogs": blogs,
        "products": products
    }
    return render_template(
        "user/profile.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )


@user_bp.route("/<user_name>")
def current_useruser(user_name):
    user = db_user.get_by_user_name(user_name=user_name)
    if not user:
        flash.error("Couldn't find a user with user name: %s" % user_name)
        return render_template(
            "base.html",
        )

    blogs = db_blog.get_blogs_for_user(user_id=user.id, limit=5, offset=0)
    products = db_product.get_blogs_for_user(user_id=user.id, limit=5, offset=0)
    props = {
        "user": dict(user),
        "blogs": blogs,
        "products": products
    }
    return render_template(
        "user/profile.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )
