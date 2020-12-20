import sqlalchemy

from hind import db
from hind.db.models.blog import Blog
from pandas import read_sql_query


def create(blog: Blog) -> int:
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            INSERT INTO blog.blog (title, user_id, body, category, upload_res_url, tags)
                 VALUES (:title, :user_id, :body, :category ,:upload_res_url, :tags)
              RETURNING id
        """), {
            "title": blog.title,
            "user_id": blog.user_id,
            "category": blog.category,
            "body": blog.body,
            "upload_res_url": blog.upload_res_url,
            "tags": blog.tags,
        })
        blog_id = result.fetchone()["id"]

    return blog_id


def get(id: int):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT *
              FROM blog.blog
             WHERE id = :blog_id
        """), {
            "blog_id": id,
        })
        row = result.fetchone()
        if not row:
            return None

        blog = dict(row)

        result = connection.execute(sqlalchemy.text("""
            SELECT count(*) as likes
              FROM blog.likes
             WHERE blog_id = :blog_id
        """), {
            "blog_id": id,
        })
        blog["likes"] = result.fetchone()["likes"]

        return Blog(**dict(blog)) if blog else None


def insert_recommendation(user_id: int, blog_id: int):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO blog.recommendations (user_id, blog_id)
                 VALUES (:user_id, :blog_id)
            ON CONFLICT (user_id, blog_id)
             DO NOTHING
        """), {
            "user_id": user_id,
            "blog_id": blog_id,
        })


def get_blogs_and_tags():
    with db.engine.connect() as connection:
        blogs = read_sql_query("""
            SELECT id, LOWER(title) AS title, category, tags
            FROM blog.blog
        """, con=connection)

        return blogs


def get_liked_blogs():
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT blog_id, user_id
            FROM blog.likes
        """), con=connection)

        return [dict(r) for r in result.fetchall()]


def like_blog(user_id: int, blog_id: int):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO blog.likes (user_id, blog_id)
                 VALUES (:user_id, :blog_id)
            ON CONFLICT (user_id, blog_id)
             DO NOTHING
        """), {
            "user_id": user_id,
            "blog_id": blog_id,
        })
