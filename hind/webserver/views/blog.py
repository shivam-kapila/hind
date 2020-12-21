import ujson

import hind.db.blog as db_blog
from flask import Blueprint, render_template, current_app, request
from flask_login import current_user, login_required
from hind.webserver.views.api_tools import _get_non_negative_param

blog_bp = Blueprint('blog', __name__)


@blog_bp.route("/<int:blog_id>")
def blog(blog_id):
    blog = db_blog.get(id=blog_id)
    props = {
        "blog": dict(blog),
    }
    return render_template(
        "blog/blog.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )


@blog_bp.route("/search")
def search():
    keyword = request.args.get("keyword")
    limit = _get_non_negative_param("limit", default=5)
    offset = request.args.get("offset", default=0)

    blogs = db_blog.search(keyword=keyword, limit=limit, offset=offset)
    current_app.logger.error(limit)
    props = {
        "current_user": current_user,
        "blogs": blogs,
        "limit": limit,
        "offset": offset
    }
    return render_template(
        "blog/search.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )
