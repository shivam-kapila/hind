import ujson
import hind.db.blog as db_blog

from hind.db.models.user import User
from hind.webserver import flash
from flask import Blueprint, render_template, current_app, request
from flask_login import current_user, login_required


user_bp = Blueprint('user', __name__)


@user_bp.route("/profile")
@login_required
def profile():
    blogs = db_blog.get_blogs_for_user(user_id=current_user.id, limit=5, offset=0)
    props = {
        "user": dict(current_user),
        "blogs": blogs,
    }
    return render_template(
        "user/profile.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )
