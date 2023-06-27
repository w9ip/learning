from app_pkg import app, db
from app_pkg.models import User, Post
import logging
from logging.handlers import SMTPHandler


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=False)
