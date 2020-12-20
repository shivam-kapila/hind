BEGIN;

ALTER TABLE blog.blog
    ADD CONSTRAINT blog_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user" (id)
    ON DELETE CASCADE;

ALTER TABLE blog.likes
    ADD CONSTRAINT blog_likes_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user" (id)
    ON DELETE CASCADE;

ALTER TABLE blog.likes
    ADD CONSTRAINT blog_likes_blog_id_foreign_key
    FOREIGN KEY (blog_id)
    REFERENCES blog.blog (id)
    ON DELETE CASCADE;

ALTER TABLE blog.recommendations
    ADD CONSTRAINT blog_recommnedation_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user" (id)
    ON DELETE CASCADE;

ALTER TABLE blog.recommendations
    ADD CONSTRAINT blog_recommendation_blog_id_foreign_key
    FOREIGN KEY (blog_id)
    REFERENCES blog.blog (id)
    ON DELETE CASCADE;

COMMIT;
