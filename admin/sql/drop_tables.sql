BEGIN;

DROP TABLE IF EXISTS "user".user CASCADE;
DROP TABLE IF EXISTS "user".supporters CASCADE;
DROP TABLE IF EXISTS blog.blog CASCADE;
DROP TABLE IF EXISTS blog.likes CASCADE;
DROP TABLE IF EXISTS blog.recommendations CASCADE;

COMMIT;
