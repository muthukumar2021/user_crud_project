from flask import Flask

app = Flask(__name__, template_folder='templates')

import user.db.model
import user.rest.user_crud
import user.validation.invalid_route