import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '8225edaef5b9b39a0694704408828f5f'