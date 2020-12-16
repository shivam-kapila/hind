DEBUG = True  # set to False in production mode

# Primary databases
SQLALCHEMY_DATABASE_URI = "postgresql://hind:hind@db:5432/hind"

POSTGRES_ADMIN_URI = "postgresql://postgres:postgres@db/postgres"
POSTGRES_ADMIN_HIND_URI = "postgresql://postgres:postgres@db/hind"

# Users who are allowed to view the LB admin interface
ADMINS = []

# expiration of 'Remember me' cookie
SESSION_REMEMBER_ME_DURATION = 365
