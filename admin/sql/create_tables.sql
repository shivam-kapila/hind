BEGIN;

CREATE TABLE "user".user (
  id                    SERIAL,
  name                  VARCHAR NOT NULL,
  user_name             VARCHAR NOT NULL,
  email_id              VARCHAR NOT NULL,
  about                 VARCHAR,
  password              VARCHAR,
  address               VARCHAR,
  profile_picture_url   VARCHAR,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  auth_token            VARCHAR NOT NULL
);
ALTER TABLE "user".user ADD CONSTRAINT user_user_name_key UNIQUE (user_name);

CREATE TABLE "user".follower (
  user_id               INT, --FK to user.id
  follower_id           INT --FK to user.id
);

CREATE TABLE blog.blog (
  id                    SERIAL,
  user_id               INT, --FK to "user".user.id
  title                 VARCHAR NOT NULL,
  location              VARCHAR,
  category              VARCHAR NOT NULL,
  body                  VARCHAR,
  upload_res_url        VARCHAR,
  tags                  TEXT[],
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE blog.like (
  user_id               INT, --FK to "user".user.id
  blog_id               INT --FK to blog.blog.id
);

CREATE TABLE blog.recommendation (
  user_id               INT, --FK to "user".user.id
  blog_id               INT --FK to blog.blog.id
);

CREATE TABLE product.product (
  id                    SERIAL,
  seller_id             INT, --FK to "user".user.id
  name                  VARCHAR NOT NULL,
  origin_location       VARCHAR,
  category              VARCHAR NOT NULL,
  description           VARCHAR,
  upload_res_url        VARCHAR,
  tags                  TEXT[],
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE product.bid (
  id                    SERIAL,
  product_id            INT, --FK to product.product.id
  starting_bid          FLOAT NOT NULL,
  bidding_date          TIMESTAMP WITH TIME ZONE NOT NULL,
  socket_id             UUID,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE product.order (
  id                    SERIAL,
  bid_id                INT, --FK to product.bid.id
  buyer_id              INT, --FK to "user".user.id
  address               VARCHAR,
  bid_amount            FLOAT NOT NULL,
  payment_id            VARCHAR,
  payment_time          TIMESTAMP WITH TIME ZONE,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE product.review (
  id                    SERIAL,
  product_id            INT, --FK to product.product.id
  user_id               INT, --FK to "user".user.id
  rating                FLOAT,
  review                VARCHAR,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE product.recommendation (
  user_id               INT, --FK to "user".user.id
  product_id            INT --FK to product.product.id
);

CREATE TABLE discussion.thread (
  id                    SERIAL,
  user_id               INT, --FK to "user".user.id
  title                 VARCHAR NOT NULL,
  location              VARCHAR,
  category              VARCHAR NOT NULL ,
  body                  VARCHAR,
  tags                  TEXT[],
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE discussion.vote (
  user_id               INT, --FK to "user".user.id
  thread_id             INT, --FK to discussion.thread.id
  feedback              INT
);

CREATE TABLE discussion.comment (
  id                    SERIAL,
  user_id               INT, --FK to "user".user.id
  thread_id             INT, --FK to discussion.thread.id
  body                  VARCHAR NOT NULL,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE discussion.comment_vote (
  user_id               INT, --FK to "user".user.id
  comment_id            INT, --FK to discussion.comment.id
  feedback              INT
);

CREATE TABLE discussion.comment_comment (
  id                    SERIAL,
  user_id               INT, --FK to "user".user.id
  comment_id            INT, --FK to discussion.comment.id
  body                  VARCHAR NOT NULL,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE discussion.recommendation (
  user_id               INT, --FK to "user".user.id
  thread_id             INT --FK to discussion.thread.id
);

COMMIT;
