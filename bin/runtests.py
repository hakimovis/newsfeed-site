#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsfeed_site.settings.testing")

    from django.core.management import call_command
    from django.conf import settings

    applen = len('newsfeed_site.apps.')

    apps_for_testing = [app[applen:] for app in settings.INSTALLED_APPS
            if app.startswith("newsfeed_site.apps")]

    call_command("test", *apps_for_testing)
