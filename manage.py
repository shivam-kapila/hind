from hind import db
from hind import webserver
import os
import click

from hind.utils import safely_import_config
safely_import_config()


@click.group()
def cli():
    pass


ADMIN_SQL_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'admin', 'sql')


@cli.command(name="init_db")
@click.option("--force", "-f", is_flag=True, help="Drop existing database and user.")
@click.option("--create-db", is_flag=True, help="Create the database and user.")
def init_db(force, create_db):
    """Initializes database.
    This process involves several steps:
    1. Table structure is created.
    2. Primary keys and foreign keys are created.
    3. Indexes are created.
    """
    from hind import config
    db.init_db_connection(config.POSTGRES_ADMIN_URI)
    if force:
        res = db.run_sql_script_without_transaction(os.path.join(ADMIN_SQL_DIR, 'drop_db.sql'))
        if not res:
            raise Exception('Failed to drop existing database and user! Exit code: %i' % res)

    if create_db or force:
        print('PG: Creating user and a database...')
        res = db.run_sql_script_without_transaction(os.path.join(ADMIN_SQL_DIR, 'create_db.sql'))
        if not res:
            raise Exception('Failed to create new database and user! Exit code: %i' % res)

        db.init_db_connection(config.POSTGRES_ADMIN_HIND_URI)
        print('PG: Creating database extensions...')
        res = db.run_sql_script_without_transaction(os.path.join(ADMIN_SQL_DIR, 'create_extensions.sql'))
    # Don't raise an exception if the extension already exists

    # application = webserver.create_app()
    # with application.app_context():
    #     print('PG: Creating schema...')
    #     db.run_sql_script(os.path.join(ADMIN_SQL_DIR, 'create_schema.sql'))

    #     print('PG: Creating tables...')
    #     db.run_sql_script(os.path.join(ADMIN_SQL_DIR, 'create_tables.sql'))

    #     print('PG: Creating primary and foreign keys...')
    #     db.run_sql_script(os.path.join(ADMIN_SQL_DIR, 'create_primary_keys.sql'))
    #     db.run_sql_script(os.path.join(ADMIN_SQL_DIR, 'create_foreign_keys.sql'))

    #     print('PG: Creating indexes...')
    #     db.run_sql_script(os.path.join(ADMIN_SQL_DIR, 'create_indexes.sql'))

        print("Done!")


if __name__ == '__main__':
    cli()
