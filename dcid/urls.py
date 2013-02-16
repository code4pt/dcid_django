from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^parliament/', include('parliament.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # Examples:
    # url(r'^$', 'daas.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)