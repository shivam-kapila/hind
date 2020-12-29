BEGIN;

CREATE UNIQUE INDEX auth_token_ndx_user ON "user".user (auth_token);
CREATE UNIQUE INDEX user_id_blog_id_ndx_blog_likes ON blog.likes (user_id, blog_id);
CREATE UNIQUE INDEX user_id_blog_id_ndx_blog_recommendations ON blog.recommendations (user_id, blog_id);

COMMIT;
