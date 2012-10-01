from django.conf.urls import patterns, url


from newsfeed_site.apps.site import views

urlpatterns = patterns('',
    url(r'^$', views.HomePage.as_view(), name='home'),
)
