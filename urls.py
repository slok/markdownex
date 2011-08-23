from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import mdex.views

urlpatterns = patterns('',
    url(r'^$', mdex.views.index),
    url(r'^md/', include('mdex.urls')),
)

#urlpatterns += staticfiles_urlpatterns()
