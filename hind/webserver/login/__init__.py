from flask import current_app
from flask_login import LoginManager, UserMixin
import hind.db.user as db_user

login_manager = LoginManager()
login_manager.login_view = 'index.login'


class User(UserMixin):
    def __init__(self, id, name, user_name, address, created, auth_token):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.address = address
        self.created = created
        self.auth_token = auth_token

    @classmethod
    def from_dbrow(cls, user):
        return cls(
            id=user['id'],
            created=user['created'],
            musicbrainz_id=user['musicbrainz_id'],
            auth_token=user['auth_token'],
            gdpr_agreed=user['gdpr_agreed'],
            login_id=user['login_id'],
        )


@login_manager.user_loader
def load_user(user_login_id):
    try:
        user = db_user.get_by_login_id(user_login_id)
    except Exception as e:
        current_app.logger.error("Error while getting user by login ID: %s", str(e), exc_info=True)
        return None
    if user:
        return User.from_dbrow(user)
    else:
        return None
