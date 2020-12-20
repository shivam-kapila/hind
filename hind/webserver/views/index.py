import ujson

from flask import Blueprint, render_template, current_app, redirect, url_for, request, jsonify
from flask_login import current_user
index_bp = Blueprint('index', __name__)


@index_bp.route("/")
def index():
    return render_template(
        "index/index.html",
    )


@index_bp.route("/login")
def login():
    return render_template(
        "index/auth.html",
    )


@index_bp.route("/signup")
def signup():
    props = {
        "active_mode": "signup",
    }
    return render_template(
        "index/auth.html",
        props=ujson.dumps(props),
    )
