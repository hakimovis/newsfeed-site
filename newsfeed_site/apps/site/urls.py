from django.conf.urls import patterns, url


from newsfeed_site.apps.site import views
from views import index
urlpatterns = patterns('',
    url(r'^$', index, name='home'),
)
