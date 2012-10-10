from newsfeed_site.settings.base import *

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'newsfeed_db.sqlite'
SESSION_COOKIE_DOMAIN = 'dj.ikito.ru'