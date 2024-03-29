import logging
import sqlalchemy

from hind import db
from hind.db.models.blog import Blog
from pandas import read_sql_query


def create(blog: Blog) -> int:
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            INSERT INTO blog.blog (title, user_id, body, category, location, upload_res_url, tags)
                 VALUES (:title, :user_id, :body, :category, :location, :upload_res_url, :tags)
              RETURNING id
        """), {
            "title": blog.title,
            "user_id": blog.user_id,
            "category": blog.category,
            "location": blog.location,
            "body": blog.body,
            "upload_res_url": blog.upload_res_url,
            "tags": blog.tags,
        })
        blog_id = result.fetchone()["id"]

    return blog_id


def get(id: int):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT blog.id, title, user_id, body, category, location, upload_res_url, tags, user_name, name, profile_picture_url
              FROM blog.blog
              JOIN "user".user
                ON blog.user_id = "user".user.id
             WHERE blog.id = :blog_id
        """), {
            "blog_id": id,
        })
        row = result.fetchone()
        if not row:
            return None

        blog = dict(row)

        result = connection.execute(sqlalchemy.text("""
            SELECT count(*) as likes
              FROM blog.like
             WHERE blog_id = :blog_id
        """), {
            "blog_id": id,
        })
        blog["likes"] = result.fetchone()["likes"]

        return Blog(**dict(blog)) if blog else None


def insert_recommendation(user_id: int, blog_id: int):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO blog.recommendation (user_id, blog_id)
                 VALUES (:user_id, :blog_id)
            ON CONFLICT (user_id, blog_id)
             DO NOTHING
        """), {
            "user_id": user_id,
            "blog_id": blog_id,
        })


def get_blogs(limit: int, offset: int):
    with db.engine.connect() as connection:
        blogs = connection.execute(sqlalchemy.text("""
            SELECT blog.id, title, user_id, body, category, location, upload_res_url, tags, user_name, name, profile_picture_url
              FROM blog.blog
              JOIN "user".user
                ON blog.blog.user_id = "user".user.id
             LIMIT :limit
            OFFSET :offset
        """), {
            "limit": limit,
            "offset": offset
        })

        return [dict(blog) for blog in blogs]


def get_blogs_for_user(user_id: int, limit: int, offset: int):
    with db.engine.connect() as connection:
        blogs = connection.execute(sqlalchemy.text("""
            SELECT blog.id, title, user_id, body, category, location, upload_res_url, tags, user_name, name, profile_picture_url
              FROM blog.blog
              JOIN "user".user
                ON blog.blog.user_id = "user".user.id
             WHERE user_id = :user_id
             LIMIT :limit
            OFFSET :offset
        """), {
            "user_id": user_id,
            "limit": limit,
            "offset": offset
        })

        return [dict(blog) for blog in blogs]


def get_liked_blogs():
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT blog_id, user_id
            FROM blog.like
        """), con=connection)

        return [dict(r) for r in result.fetchall()]


def like_blog(user_id: int, blog_id: int):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO blog.like (user_id, blog_id)
                 VALUES (:user_id, :blog_id)
            ON CONFLICT (user_id, blog_id)
             DO NOTHING
        """), {
            "user_id": user_id,
            "blog_id": blog_id,
        })


def search(keyword: str, limit: int, offset: int):
    keyword_with_modulus = "%" + keyword + "%"

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT blog.id, title, user_id, body, category, location, upload_res_url, tags, user_name, name, profile_picture_url
              FROM blog.blog
              JOIN "user".user
                ON blog.blog.user_id = "user".user.id
             WHERE LOWER(title) LIKE :keyword_with_modulus
                OR LOWER(location) LIKE :keyword_with_modulus
                OR LOWER(category::text) LIKE :keyword_with_modulus
                OR :keyword = ANY(tags)
             LIMIT :limit
            OFFSET :offset
        """), {
            "keyword": keyword,
            "keyword_with_modulus": keyword_with_modulus,
            "limit": limit,
            "offset": offset
        })

        blogs = [dict(row) for row in result.fetchall()]
        return blogs
