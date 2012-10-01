from newsfeed_site.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

INSTALLED_APPS += ('sentry,')

DATABASES['default']['NAME'] = 'newsfeed_site_production'

SENTRY_LOG_DIR = os.path.join(PROJECT_DIR, 'logs')
SENTRY_RUN_DIR= os.path.join(PROJECT_DIR, 'run')
SENTRY_WEB_HOST = '127.0.0.1'
SENTRY_WEB_PORT = 9000
SENTRY_KEY = 'fktr%c-u)k#2=3h-2$*_ia!7@$*i9i@8ll^--o^&amp;n0b+7-1-*@'

SENTRY_FILTERS = (
    'sentry.filters.StatusFilter',
    'sentry.filters.LoggerFilter',
    'sentry.filters.LevelFilter',
    'sentry.filters.ServerNameFilter',
    'sentry.filters.SiteFilter',
)

SENTRY_VIEWS = (
    'sentry.views.Exception',
    'sentry.views.Message',
    'sentry.views.Query',
)


