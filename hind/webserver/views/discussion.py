import ujson

import hind.db.discussion as db_discussion
from flask import Blueprint, render_template, current_app, request, redirect, url_for
from flask_login import current_user, login_required
from hind.webserver.views.api_tools import _get_non_negative_param
from hind.db.models.discussion import Discussion
from hind.webserver import flash
from flask_login import current_user, login_required

discussion_bp = Blueprint('discussions', __name__)


@discussion_bp.route("/<int:thread_id>")
def discussion(thread_id):
    discussion = db_discussion.get(id=thread_id)
    if not discussion:
        flash.error("Couldn't find a discussion with ID: %s" % thread_id)
        return render_template(
            "base.html",
        )
    props = {
        "discussion": dict(discussion),
    }
    return render_template(
        "discussion/discussion.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )


@discussion_bp.route("/<int:thread_id>/comment", methods=["POST"])
@login_required
def comment(thread_id):
    body = request.form.get("body")

    try:
        db_discussion.insert_comment(thread_id=thread_id, user_id=current_user.id, body=body)
    except Exception as e:
        flash.error(e)
        return redirect(url_for('discussions.discussion', thread_id=thread_id))
    return redirect(url_for('discussions.discussion', thread_id=thread_id))


@discussion_bp.route("/<int:thread_id>/comment/<int:comment_id>/comment", methods=["POST"])
@login_required
def sub_comment(thread_id, comment_id):
    body = request.form.get("body")

    try:
        db_discussion.insert_sub_comment(comment_id=comment_id, user_id=current_user.id, body=body)
    except Exception as e:
        flash.error(e)
        return redirect(url_for('discussions.discussion', thread_id=thread_id))
    return redirect(url_for('discussions.discussion', thread_id=thread_id))


@discussion_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        title = request.form.get("title")
        # location = request.form.get("location")
        body = request.form.get("body")
        tags = request.form.get("tags")

        try:
            thread_id = db_discussion.create(Discussion(
                title=title,
                user_id=current_user.id,
                category="food",
                body=body,
                tags=["food"]
            ))
            return redirect(url_for('discussions.discussion', thread_id=thread_id))

        except Exception as e:
            flash.error(e)
            return render_template(
                "discussion/new_discussion.html",
            )
    return render_template(
        "discussion/new_discussion.html",
    )


@discussion_bp.route("/")
def index():
    limit = _get_non_negative_param("limit", default=5)
    offset = _get_non_negative_param("offset", default=0)

    discussions = db_discussion.get_threads(limit=limit, offset=offset)
    props = {
        "search_type": "discussion",
        "current_user": current_user,
        "discussions": discussions,
        "limit": limit,
        "offset": offset
    }
    return render_template(
        "index/search.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )
