from django.conf.urls.defaults import patterns, include, url
import mdex.views

urlpatterns = patterns('',
    url(r'^$', mdex.views.mdForm),

) 
