from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

ALLOWED_HOSTS = ['*']


# Database Connection And Configuration Using Environs

# DATABASES['default']=env.dj_db_url("DATABASE_URL")
DATABASES = {"default": env.dj_db_url("POSTGRES_URL")}

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)



# Gmail or google configuration
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='bigibraeh@gmail.com'
EMAIL_HOST_PASSWORD= 'whteyunvthmbzsvc'
EMAIL_USE_TLS=True


ADMINS = (
('Antonio M', 'email@mydomain.com'),
)