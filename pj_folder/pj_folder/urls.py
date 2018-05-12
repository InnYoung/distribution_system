from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tiger_distribution.views.home', name='home'),
    url(r'^lists/id/$', 'tiger_distribution.views.view_list', name='view_list')
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
