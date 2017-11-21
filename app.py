"""Trivial flask app to demonstrate how to use ox_herd.
"""

import logging
import random

from flask import Flask, Markup, url_for

# The following imports a settings module and a simple login_stub module so
# we can have at least a tiny bit of security for our example.
from passlib.apps import custom_app_context
from ox_herd import settings
from ox_herd.core import login_stub

# The following line imports the ox_herd views which registers routes.
from ox_herd.ui.flask_web_ui.ox_herd import views as ox_herd_views

# The following imports the ox_herd blueprint.
from ox_herd.ui.flask_web_ui.ox_herd import OX_HERD_BP

APP = Flask(__name__)

@APP.route('/')
@login_stub.login_required
def index():
    """Route for main index.

    This basically serves as the root and points the user to the ox_herd
    blueprint inside the main app.
    """
    oh_index = url_for('ox_herd.index')
    link = '<A HREF="%s">%s</A>' % (oh_index, oh_index)
    msg = Markup('Welcome to ox_herd_example! Interesting stuff is at %s.' % (
        link))
    return msg


def setup_app(my_app):
    """Setup the flask app.

    Mostly this is setting up a simple username/password. This will be
    logged to the console so you can go to http://127.0.0.1:5000/login
    and login. For your purposes, you can just hard code the password
    below instead of randomly generating it, but since this is on github
    we do not want to hard code the password.
    """
    login_url = 'http://127.0.0.1:5000/login'
    logging.info('Registered views in %s', str(ox_herd_views))
    random_pw = str(random.randint(1, 1 << 128))
    pw_hash = custom_app_context.encrypt(random_pw)
    logging.warning('Login at %s using username=%s and random password "%s"',
                    login_url, 'test_user', random_pw)
    settings.STUB_USER_DB['test_user'] = pw_hash

    # Flask requiers you to set a secret key for sessions to work.
    my_app.secret_key = str(random.randint(1, 1 << 256))

    # Append our example_plugins.py module to list of plugins to load.
    settings.OX_PLUGINS.append('example_plugins')

    # Register the ox_herd blueprint
    my_app.register_blueprint(OX_HERD_BP)

    # Register the login stub
    my_app.register_blueprint(login_stub.LOGIN_STUB_BP)


if __name__ == '__main__':
    setup_app(APP)
    APP.run(host='0.0.0.0')
