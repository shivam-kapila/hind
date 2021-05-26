import sqlalchemy

from hind import db
from hind.db.models.product import Product


def create(product: Product) -> int:
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            INSERT INTO product.product (name, seller_id, description, category, origin_location, upload_res_url, tags)
                 VALUES (:name, :user_id, :description, :category, :origin_location, :upload_res_url, :tags)
              RETURNING id
        """), {
            "name": product.name,
            "seller_id": product.user_id,
            "category": product.category,
            "origin_location": product.origin_location,
            "description": product.description,
            "upload_res_url": product.upload_res_url,
            "tags": product.tags,
        })
        product_id = result.fetchone()["id"]

    return product_id


def get(id: int):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT product.id
                 , product.name
                 , seller_id
                 , description
                 , category
                 , origin_location
                 , upload_res_url
                 , tags
                 , user_name
                 , "user".name AS name_of_user
                 , profile_picture_url
              FROM product.product
              JOIN "user".user
                ON product.seller_id = "user".user.id
             WHERE product.id = :product_id
        """), {
            "product_id": id,
        })
        row = result.fetchone()
        if not row:
            return None

        product = dict(row)

        bids = connection.execute(sqlalchemy.text("""
            SELECT bid.id
                 , starting_bid
                 , bidding_date
                 , starting_bid
                 , user_name
                 , "user".name AS name_of_user
                 , profile_picture_url
              FROM product.bid, product.product
              JOIN "user".user
                ON product.product.seller_id = "user".user.id
             WHERE product_id = :product_id
          ORDER BY bidding_date DESC
        """), {
            "product_id": product["id"],
        })

        product["bids"] = [dict(r) for r in bids.fetchall()]

        return Product(**dict(product)) if product else None


def insert_recommendation(user_id: int, product_id: int):
    with db.engine.connect() as connection:
        connection.execute(sqlalchemy.text("""
            INSERT INTO product.recommendation (user_id, product_id)
                 VALUES (:user_id, :product_id)
            ON CONFLICT (user_id, product_id)
             DO NOTHING
        """), {
            "user_id": user_id,
            "product_id": product_id,
        })


def get_products(limit: int, offset: int):
    with db.engine.connect() as connection:
        products = connection.execute(sqlalchemy.text("""
            SELECT product.id
                 , product.name
                 , seller_id
                 , description
                 , category
                 , origin_location
                 , upload_res_url
                 , tags
                 , user_name
                 , "user".name
                 , profile_picture_url
              FROM product.product
              JOIN "user".user
                ON product.product.seller_id = "user".user.id
             LIMIT :limit
            OFFSET :offset
        """), {
            "limit": limit,
            "offset": offset
        })

        return [dict(product) for product in products]


def get_products_for_user(user_id: int, limit: int, offset: int):
    with db.engine.connect() as connection:
        products = connection.execute(sqlalchemy.text("""
            SELECT product.id
                 , product.name
                 , seller_id
                 , description
                 , category
                 , origin_location
                 , upload_res_url
                 , tags
                 , user_name
                 , "user".name
                 , profile_picture_url
              FROM product.product
              JOIN "user".user
                ON product.product.seller_id = "user".user.id
             WHERE seller_id = :user_id
             LIMIT :limit
            OFFSET :offset
        """), {
            "user_id": user_id,
            "limit": limit,
            "offset": offset
        })

        return [dict(product) for product in products]


def search(keyword: str, limit: int, offset: int):
    keyword_with_modulus = "%" + keyword + "%"

    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT product.id
                 , product.name
                 , seller_id
                 , description
                 , category
                 , origin_location
                 , upload_res_url
                 , tags
                 , user_name
                 , "user".name
                 , profile_picture_url
              FROM product.product
              JOIN "user".user
                ON product.product.seller_id = "user".user.id
             WHERE LOWER(product.name) LIKE :keyword_with_modulus
                OR LOWER(origin_location) LIKE :keyword_with_modulus
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

        products = [dict(row) for row in result.fetchall()]
        return products
