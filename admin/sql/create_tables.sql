BEGIN;

CREATE TABLE "user" (
  id                    SERIAL,
  name                  VARCHAR,
  email_id              VARCHAR,
  password_hash         VARCHAR,
  address               JSONB,
  created               TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  auth_token            VARCHAR
);

COMMIT;
