from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('parliament.views', #prefix
	url(r'^$', 'index'),
	url(r'^tags/$', 'tags'),
	url(r'^tags/(?P<tag_name>\S+)/$', 'tag_detail'),
    url(r'^proposals/$', 'proposals'),
    url(r'^proposals/(?P<proposal_id>\d+)/$', 'proposal_detail'),
    url(r'^proposals/create/$', 'proposal_create'),
    url(r'^proposals/vote/(?P<proposal_id>\d+)/(?P<vote_direction>\S+)/$', 'proposal_vote'),
)

urlpatterns += staticfiles_urlpatterns()