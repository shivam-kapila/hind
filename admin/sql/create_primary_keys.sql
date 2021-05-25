BEGIN;

ALTER TABLE "user".user ADD CONSTRAINT user_pkey PRIMARY KEY (id);

ALTER TABLE blog.blog ADD CONSTRAINT blog_pkey PRIMARY KEY (id);

ALTER TABLE product.product ADD CONSTRAINT product_pkey PRIMARY KEY (id);
ALTER TABLE product.bid ADD CONSTRAINT product_bid_pkey PRIMARY KEY (id);
ALTER TABLE product.order ADD CONSTRAINT product_order_pkey PRIMARY KEY (id);
ALTER TABLE product.review ADD CONSTRAINT product_review_pkey PRIMARY KEY (id);

ALTER TABLE discussion.thread ADD CONSTRAINT discussion_thread_pkey PRIMARY KEY (id);
ALTER TABLE discussion.comment ADD CONSTRAINT discussion_comment_pkey PRIMARY KEY (id);
ALTER TABLE discussion.comment_comment ADD CONSTRAINT discussion_comment_comment_pkey PRIMARY KEY (id);

COMMIT;
