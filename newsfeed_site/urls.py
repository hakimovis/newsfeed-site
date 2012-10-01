from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('newsfeed_site.apps.site.urls', namespace='site')),
    url(r'^admin/', include(admin.site.urls)),
)
