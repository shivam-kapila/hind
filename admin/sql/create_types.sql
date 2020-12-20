BEGIN;

CREATE TYPE blog_category AS ENUM('local trivia', 'my creations', 'historical significance');

COMMIT;