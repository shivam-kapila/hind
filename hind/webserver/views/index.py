import ujson
from datetime import timedelta
from flask import Blueprint, render_template, current_app, redirect, request, url_for, session
from flask_login import current_user, login_user, login_required, logout_user

import hind.db.user as db_user
import hind.db.blog as db_blog
import hind.db.product as db_product
import hind.db.discussion as db_discussion
from hind.db.models.user import User
from hind.webserver import flash
from hind.webserver.views.api_tools import _get_non_negative_param

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
            return redirect(url_for('user.profile'))

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

        try:
            user_id = db_user.create(User(
                name=name,
                user_name=user_name,
                password=password,
                email_id=email_id,
                address=address,
            ))

        except Exception as e:
            flash.error(e._message)
            return render_template(
                "index/auth.html",
                props=ujson.dumps(props),
            )

        user = db_user.get_by_id(id=user_id)
        login_user(user, remember=True, duration=timedelta(current_app.config['SESSION_REMEMBER_ME_DURATION']))

        flash.success('Hey there! Welcome to hind!')
        return redirect(url_for('user.profile'))

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


@index_bp.route("/search")
def search():
    keyword = request.args.get("keyword")
    search_type = request.args.get("type")
    limit = _get_non_negative_param("limit", default=5)
    offset = _get_non_negative_param("offset", default=0)

    blogs = []
    products = []
    discussions = []

    if search_type:
        if search_type == "blog":
            blogs = db_blog.search(keyword=str.lower(keyword), limit=limit, offset=offset)

        elif search_type == "product":
            products = db_product.search(keyword=str.lower(keyword), limit=limit, offset=offset)

        elif search_type == "discussion":
            discussions = db_discussion.search(keyword=str.lower(keyword), limit=limit, offset=offset)

        else:
            flash.error("Invalid search type: %s" % search_type)
            return render_template(
                "base.html",
            )
    else:
        blogs = db_blog.search(keyword=str.lower(keyword), limit=limit, offset=offset)
        products = db_product.search(keyword=str.lower(keyword), limit=limit, offset=offset)
        discussions = db_discussion.search(keyword=str.lower(keyword), limit=limit, offset=offset)

    props = {
        "keyword": keyword,
        "search_type": search_type,
        "current_user": current_user,
        "blogs": blogs,
        "products": products,
        "discussions": discussions,
        "limit": limit,
        "offset": offset
    }
    return render_template(
        "index/search.html",
        current_user=current_user,
        props=ujson.dumps(props),
    )
