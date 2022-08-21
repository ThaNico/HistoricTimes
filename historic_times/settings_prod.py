import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["127.0.0.1", "historic-times.herokuapp.com"]

# if https:
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url # noqa
from django.conf import settings  # noqa
db_from_env = dj_database_url.config(conn_max_age=500)
settings.DATABASES['default'].update(db_from_env)


# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = settings.BASE_DIR / 'staticfiles'
# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'
# Simplified static file serving.
# https://pypi.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
