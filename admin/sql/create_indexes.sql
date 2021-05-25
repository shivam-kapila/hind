BEGIN;

CREATE UNIQUE INDEX auth_token_ndx_user ON "user".user (auth_token);
CREATE UNIQUE INDEX user_id_follower_id_ndx_user_follower ON "user".follower (user_id, follower_id);

CREATE UNIQUE INDEX user_id_blog_id_ndx_blog_like ON blog.like (user_id, blog_id);
CREATE UNIQUE INDEX user_id_blog_id_ndx_blog_recommendation ON blog.recommendation (user_id, blog_id);

CREATE UNIQUE INDEX user_id_product_id_ndx_product_recommendation ON product.recommendation (user_id, product_id);

CREATE UNIQUE INDEX user_id_thread_id_ndx_thread_recommendation ON discussion.recommendation (user_id, thread_id);
CREATE UNIQUE INDEX user_id_thread_id_ndx_discussion_vote ON discussion.vote (user_id, thread_id);
CREATE UNIQUE INDEX user_id_thread_id_ndx_discussion_comment_vote ON discussion.comment_vote (user_id, comment_id);

COMMIT;
