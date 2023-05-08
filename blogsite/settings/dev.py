from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Ways To Define Database Using Environs

DATABASES = {"default": env.dj_db_url("SQLITE_URL")}

# DATABASES = {}
# DATABASES['default']=env.dj_db_url('SQLITE_URL', default="sqlite:///"+os.path.join(BASE_DIR, 'dbblog.sqlite3'), ssl_require=not DEBUG)


# Defining Database Using Dj_database_url Parsing And Config Method.

# DATABASES['default']=dj_database_url.parse('sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3'))
# DATABASES['default']=dj_database_url.config() # Config needs DATABASE_URL to be set 
# print(DATABASES)


# Gmail or email configuration
# email = dj_email_url.config()
email = env.dj_email_url("EMAIL_URL", default="smtp://")

EMAIL_BACKEND= email['EMAIL_BACKEND']
EMAIL_HOST= email["EMAIL_HOST"]
EMAIL_PORT= email["EMAIL_PORT"]
EMAIL_HOST_USER= email["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD= email["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS= email["EMAIL_USE_SSL"]


# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT=587
# EMAIL_HOST_USER='bigibraeh@gmail.com'
# EMAIL_HOST_PASSWORD= 'whteyunvthmbzsvc'
# EMAIL_USE_TLS=True

# url = 'smtp://user@domain.com:pass@smtp.example.com:465/?ssl=True'
# url = dj_email_url.parse(url)
# for u,v in url.items():
# 	print (u,":", v)