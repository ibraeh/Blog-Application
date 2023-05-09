from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

ALLOWED_HOSTS = ['*']


# Database Connection And Configuration Using Environs

# DATABASES['default']=env.dj_db_url("DATABASE_URL")
DATABASES = {"default": env.dj_db_url("POSTGRES_URL")}

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)



# Gmail or email configuration
# email = dj_email_url.config()
email = env.dj_email_url("EMAIL_URL", default="smtp://")

EMAIL_BACKEND= email['EMAIL_BACKEND']
EMAIL_HOST= email["EMAIL_HOST"]
EMAIL_PORT= email["EMAIL_PORT"]
EMAIL_HOST_USER= email["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD= email["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS= email["EMAIL_USE_SSL"]


ADMINS = (
('Antonio M', 'email@mydomain.com'),
)

# CACHES = {"default": env.dj_cache_url("CACHE_URL")}