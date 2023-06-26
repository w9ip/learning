import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yoo\'ll-never-guess'
    print(SECRET_KEY)