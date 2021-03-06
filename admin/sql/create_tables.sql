BEGIN;

CREATE TABLE "user".user (
  id                    SERIAL,
  name                  VARCHAR,
  user_name             VARCHAR,
  email_id              VARCHAR,
  about                 VARCHAR,
  password              VARCHAR,
  address               VARCHAR,
  profile_picture_url   VARCHAR,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  auth_token            VARCHAR
);
ALTER TABLE "user".user ADD CONSTRAINT user_user_name_key UNIQUE (user_name);

CREATE TABLE "user".supporters (
  user_id               INT, --FK to user.id
  supporter_id          INT --FK to user.id
);

CREATE TABLE blog.blog (
  id                    SERIAL,
  user_id               INT, --FK to "user".user.id
  title                 VARCHAR,
  location              VARCHAR,
  category              blog_category,
  body                  VARCHAR,
  upload_res_url        VARCHAR,
  tags                  TEXT[],
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE blog.likes (
  user_id               INT, --FK to "user".user.id
  blog_id               INT --FK to blog.id
);

CREATE TABLE blog.recommendations (
  user_id               INT, --FK to "user".user.id
  blog_id               INT --FK to blog.id
);

COMMIT;
