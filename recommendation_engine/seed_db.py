import hind.db.blog as db_blog
import hind.db.user as db_user

from hind.db.models.user import User
from hind.db.models.blog import Blog
from random import randint
from recommendation_engine.faker_config import fake

FAKE_USERS = 50
MAX_FAKE_BLOGS_PER_USER = 20
MAX_LIKES_PER_USER = 10


class SeedDB():
    def create_fake_users(self):
        for i in range(FAKE_USERS):
            fake_user = fake.simple_profile()
            user = User(
                        name=fake_user['name'],
                        user_name=fake_user['username'],
                        email_id=fake_user['mail'],
                        about=fake.text(),
                        password=fake_user['username'],
                        address=(fake_user['address']).replace("\n", " "),
                        )

            db_user.create(user=user)

    def create_fake_blogs(self):
        count = 0
        for i in range(1, FAKE_USERS):
            for j in range(randint(1, MAX_FAKE_BLOGS_PER_USER)):
                blog = Blog(
                    title=fake.sentence(),
                    user_id=i,
                    category=fake.category(),
                    body=fake.text(),
                    tags=fake.tags(),
                    upload_res_url=fake.image_url(),
                )
                db_blog.create(blog=blog)
                count += 1

        return count

    def create_fake_likes(self, blog_count: int):
        for i in range(1, FAKE_USERS):
            for j in range(randint(1, MAX_LIKES_PER_USER)):
                k = randint(1, blog_count)
                db_blog.like_blog(user_id=i, blog_id=k)
