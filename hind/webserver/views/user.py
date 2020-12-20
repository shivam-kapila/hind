
from hind.db.models.user import User
from hind.webserver import flash
from flask import Blueprint, render_template, current_app, request
from flask_login import current_user, login_required


user_bp = Blueprint('user', __name__)


@user_bp.route("/profile")
def index():
    current_app.logger.error(current_user.is_authenticated)
    return render_template(
        "user/user.html",
        current_user=current_user
    )
