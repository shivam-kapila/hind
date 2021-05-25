BEGIN;

ALTER TABLE "user".follower
    ADD CONSTRAINT follower_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE "user".follower
    ADD CONSTRAINT follower_follower_id_foreign_key
    FOREIGN KEY (follower_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE blog.blog
    ADD CONSTRAINT blog_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE blog.like
    ADD CONSTRAINT blog_like_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE blog.like
    ADD CONSTRAINT blog_like_blog_id_foreign_key
    FOREIGN KEY (blog_id)
    REFERENCES blog.blog (id)
    ON DELETE CASCADE;

ALTER TABLE blog.recommendation
    ADD CONSTRAINT blog_recommendation_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE blog.recommendation
    ADD CONSTRAINT blog_recommendation_blog_id_foreign_key
    FOREIGN KEY (blog_id)
    REFERENCES blog.blog (id)
    ON DELETE CASCADE;

ALTER TABLE product.product
    ADD CONSTRAINT product_seller_id_foreign_key
    FOREIGN KEY (seller_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE product.bid
    ADD CONSTRAINT product_bid_product_id_foreign_key
    FOREIGN KEY (product_id)
    REFERENCES product.product (id)
    ON DELETE CASCADE;

ALTER TABLE product.order
    ADD CONSTRAINT product_order_buyer_id_foreign_key
    FOREIGN KEY (buyer_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE product.order
    ADD CONSTRAINT product_order_bid_id_foreign_key
    FOREIGN KEY (bid_id)
    REFERENCES product.bid (id)
    ON DELETE CASCADE;

ALTER TABLE product.recommendation
    ADD CONSTRAINT product_recommendation_product_id_foreign_key
    FOREIGN KEY (product_id)
    REFERENCES product.product (id)
    ON DELETE CASCADE;

ALTER TABLE product.recommendation
    ADD CONSTRAINT product_recommendation_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.thread
    ADD CONSTRAINT discussion_thread_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.vote
    ADD CONSTRAINT discussion_vote_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.vote
    ADD CONSTRAINT  discussion_vote_thread_id_foreign_key
    FOREIGN KEY (thread_id)
    REFERENCES discussion.thread (id)
    ON DELETE CASCADE;


ALTER TABLE discussion.comment
    ADD CONSTRAINT discussion_comment_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.comment
    ADD CONSTRAINT  discussion_comment_thread_id_foreign_key
    FOREIGN KEY (thread_id)
    REFERENCES discussion.thread (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.comment_vote
    ADD CONSTRAINT discussion_comment_vote_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.comment_vote
    ADD CONSTRAINT  discussion_comment_vote_comment_id_foreign_key
    FOREIGN KEY (comment_id)
    REFERENCES discussion.comment (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.comment_comment
    ADD CONSTRAINT discussion_comment_comment_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.comment_comment
    ADD CONSTRAINT  discussion_comment_comment_comment_id_foreign_key
    FOREIGN KEY (comment_id)
    REFERENCES discussion.comment (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.recommendation
    ADD CONSTRAINT discussion_recommendation_thread_id_foreign_key
    FOREIGN KEY (thread_id)
    REFERENCES discussion.thread (id)
    ON DELETE CASCADE;

ALTER TABLE discussion.recommendation
    ADD CONSTRAINT discussion_recommendation_user_id_foreign_key
    FOREIGN KEY (user_id)
    REFERENCES "user".user (id)
    ON DELETE CASCADE;

COMMIT;
