from django.conf.urls import patterns, include, url
#from django.contrib import admin
from bigbenchtheory.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bigbenchtheory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', sub)
)
