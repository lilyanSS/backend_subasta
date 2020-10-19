
from .common import *
import environ


env = environ.Env()


base = environ.Path(__file__) - 4
environ.Env.read_env(env_file=base('.env'))


DEBUG = True

DATABASES = {
    'default': {
        # MySQL database engine class.
        'ENGINE': 'django.db.backends.mysql',
        # MySQL database host ip.
        'HOST': env.str('DB_HOST'),
        # port number.
        'PORT': env.str('DB_PORT'),
        # database name.
        'NAME': env.str('DB_NAME'),
        # user name.
        'USER': env.str('DB_USER'),
        # password
        'PASSWORD': env.str('DB_PASSWORD'),
        # connect options
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", },
    }
}
