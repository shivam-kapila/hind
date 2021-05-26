import sqlalchemy

from hind import db
from hind.db.models.discussion import Discussion


def create(thread: Discussion) -> int:
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            INSERT INTO discussion.thread (title, user_id, body, category, location, tags)
                 VALUES (:title, :user_id, :body, :category, :location, :tags)
              RETURNING id
        """), {
            "title": thread.title,
            "user_id": thread.user_id,
            "category": thread.category,
            "location": thread.location,
            "body": thread.body,
            "tags": thread.tags,
        })
        thread_id = result.fetchone()["id"]

    return thread_id


def get(id: int):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT thread.id, title, user_id, body, category, location, tags, user_name, name, profile_picture_url
              FROM discussion.thread
              JOIN "user".user
                ON thread.user_id = "user".user.id
             WHERE thread.id = :thread_id
        """), {
            "thread_id": id,
        })
        row = result.fetchone()
        return dict(row) if row else None


def insert_recommendation(user_id: int, thread_id: int):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO thread.recommendation (user_id, thread_id)
                 VALUES (:user_id, :thread_id)
            ON CONFLICT (user_id, thread_id)
             DO NOTHING
        """), {
            "user_id": user_id,
            "thread_id": thread_id,
        })


def get_threads(limit: int, offset: int):
    with db.engine.connect() as connection:
        threads = connection.execute(sqlalchemy.text("""
            SELECT thread.id, title, user_id, body, category, location, tags, user_name, name, profile_picture_url
              FROM discussion.thread
              JOIN "user".user
                ON discussion.thread.user_id = "user".user.id
             LIMIT :limit
            OFFSET :offset
        """), {
            "limit": limit,
            "offset": offset
        })

        return [dict(thread) for thread in threads]


def get_threads_for_user(user_id: int, limit: int, offset: int):
    with db.engine.connect() as connection:
        threads = connection.execute(sqlalchemy.text("""
            SELECT thread.id, title, user_id, body, category, location, tags, user_name, name, profile_picture_url
              FROM discussion.thread
              JOIN "user".user
                ON discussion.thread.user_id = "user".user.id
             WHERE user_id = :user_id
             LIMIT :limit
            OFFSET :offset
        """), {
            "user_id": user_id,
            "limit": limit,
            "offset": offset
        })

        return [dict(thread) for thread in threads]


def insert_comment(thread_id: int, user_id: int, body: str):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO discussion.comment (thread_id, user_id, body)
                 VALUES (:thread_id, :user_id, :body)
              RETURNING id
        """), {
            "thread_id": thread_id,
            "user_id": user_id,
            "body": body,
        })


def insert_sub_comment(comment_id: int, user_id: int, body: str):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO discussion.comment_comment (comment_id, user_id, body)
                 VALUES (:comment_id, :user_id, :body)
              RETURNING id
        """), {
            "comment_id": comment_id,
            "user_id": user_id,
            "body": body,
        })


def search(keyword: str, limit: int, offset: int):
    keyword_with_modulus = "%" + keyword + "%"

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT thread.id, title, user_id, body, category, location, tags, user_name, name, profile_picture_url
              FROM discussion.thread
              JOIN "user".user
                ON discussion.thread.user_id = "user".user.id
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

        discussions = [dict(row) for row in result.fetchall()]
        return discussions
