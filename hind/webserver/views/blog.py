import ujson

import hind.db.blog as db_blog
from flask import Blueprint, render_template, current_app, request, redirect, url_for
from flask_login import current_user, login_required
from hind.webserver.views.api_tools import _get_non_negative_param
from hind.db.models.blog import Blog
from hind.webserver import flash
from flask_login import current_user, login_required

blog_bp = Blueprint('blogs', __name__)


@blog_bp.route("/<int:blog_id>")
def blog(blog_id):
    blog = db_blog.get(id=blog_id)
    if not blog:
        flash.error("Couldn't find a blog with ID: %s" % blog_id)
        return render_template(
            "base.html",
        )
    props = {
        "blog": dict(blog),
    }
    return render_template(
        "blog/blog.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )


@blog_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        title = request.form.get("title")
        # category = request.form.get("user_name")
        location = request.form.get("location")
        body = request.form.get("body")
        tags = request.form.get("tags")
        current_app.logger.debug(current_user)
        try:
            blog_id = db_blog.create(Blog(
                title=title,
                user_id=current_user.id,
                category="local trivia",
                location=location,
                body=body,
                upload_res_url="https://placeimg.com/152/97/any",
                tags=["food"]
            ))
            return redirect(url_for('blogs.blog', blog_id=blog_id))

        except Exception as e:
            flash.error(e)
            return render_template(
                "blog/new_blog.html",
            )
    return render_template(
        "blog/new_blog.html",
    )


@blog_bp.route("/")
def index():
    limit = _get_non_negative_param("limit", default=5)
    offset = _get_non_negative_param("offset", default=0)

    blogs = db_blog.get_blogs(limit=limit, offset=offset)
    props = {
        "search_type": "blog",
        "current_user": current_user,
        "blogs": blogs,
        "limit": limit,
        "offset": offset
    }
    return render_template(
        "index/search.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )
