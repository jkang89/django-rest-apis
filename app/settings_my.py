try:
    from app.settings import *
except ImportError, exp:
    pass

DEBUG = True
SECRET_KEY = ';^E|p>s@$3<G=PrKPgS9}S!DkzjY&?;VKv_9Ue>)JMmfaCel$;'

SOCIAL_AUTH_TWITTER_KEY = 'KjSUQMOfgS8lbnpOqE0elmn2o'
SOCIAL_AUTH_TWITTER_SECRET = 'XBxOmG87UgYfgQDSSSEdD7cIoFUj9rJG2XHEsbV4TjWpfIorR4'

TWITTER_ACCESS_TOKEN = '2155490413-XWMJqPMEqiGIh9Vdt1yT8GKQOqOOTWHfh3sQyZo'
TWITTER_ACCESS_TOKEN_SECRET = 'T0QcyOfyx4hRV2ZfXzfAx8AK61lCMAGkxy3T2OgQLcY5Y'

GNIP_USERNAME = ""
GNIP_PASSWORD = ""
GNIP_SEARCH_ENDPOINT = ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}