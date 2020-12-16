-- Create the user and the database. Must run as user postgres.

CREATE USER hind NOCREATEDB NOSUPERUSER;
ALTER USER hind WITH PASSWORD 'hind';
CREATE DATABASE hind WITH OWNER = hind TEMPLATE template0 ENCODING = 'UNICODE';
