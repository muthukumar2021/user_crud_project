from user import app
from user.db.model import db
from user.multi_lang_response.multi_lang_response import get_response_data


def create_app():
    db.create_all()
    get_response_data()


# flask run
print(f'ENV is set to: {app.config["ENV"]}')
print(app.config)
create_app()
