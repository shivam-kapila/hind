import ujson
import hind.db.user as db_user
from datetime import timedelta
from hind.db.models.user import User
from hind.webserver import flash
from flask import Blueprint, render_template, current_app, redirect, request, url_for, session
from flask_login import current_user, login_user, login_required, logout_user

index_bp = Blueprint('index', __name__)


@index_bp.route("/")
def index():
    return render_template(
        "index/index.html",
        class_name="landing"
    )


@index_bp.route("/login", methods=["GET", "POST"])
def login():
    props = {
        "active_mode": "login",
    }

    if request.method == "POST":
        user_name = request.form.get("user_name")
        password = request.form.get("password")

        user = db_user.get(User(user_name=user_name, password=password))
        if user:
            login_user(user, remember=True, duration=timedelta(current_app.config['SESSION_REMEMBER_ME_DURATION']))
            flash.success('Hey there! Welcome back!')
            return redirect(url_for('user.index'))

        flash.error('Username or password incorrect! Please try again')

    return render_template(
        "index/auth.html",
        props=ujson.dumps(props),
        current_user=current_user
    )


@index_bp.route("/signup", methods=["GET", "POST"])
def signup():
    props = {
        "active_mode": "signup",
    }

    if request.method == "POST":
        name = request.form.get("name")
        user_name = request.form.get("user_name")
        email_id = request.form.get("email_id")
        password = request.form.get("password")
        address = request.form.get("address")
        about = request.form.get("user_name")
        user_id = -1

        try:
            user_id = db_user.create(User(
                name=name,
                user_name=user_name,
                password=password,
                email_id=email_id,
                address=address,
                about=about
            ))

        except Exception as e:
            flash.error(e)
            return render_template(
                "index/auth.html",
                props=ujson.dumps(props),
            )

        user = db_user.get_by_id(id=user_id)
        login_user(user, remember=True, duration=timedelta(current_app.config['SESSION_REMEMBER_ME_DURATION']))

        flash.success('Hey there! Welcome to hind!')
        return redirect(url_for('user.index'))

    return render_template(
        "index/auth.html",
        props=ujson.dumps(props),
    )


@index_bp.route('/logout/')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('index.index'))
