from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('parliament.views',  # prefix
	# Home
	url(r'^$', 'index'),
	
	# Tags
	url(r'^tags/$', 'tags'),
	url(r'^tags/(?P<tag_name>\S+)/$', 'tag_detail'),
	
	# Proposals
    url(r'^proposals/$', 'proposals'),
    url(r'^proposals/(?P<proposal_id>\d+)/$', 'proposal_detail'),
    url(r'^proposals/create/$', 'proposal_create'),
    url(r'^proposals/vote/(?P<proposal_id>\d+)/(?P<vote_direction>\S+)/$', 'proposal_vote'),
    
    # Authentication
    url(r'^user/login/$', 'login'),
    url(r'^user/login/auth/$', 'auth_view'),
    url(r'^user/login/success/$', 'login_success'),
    url(r'^user/login/invalid/$', 'login_invalid'),
    url(r'^user/logout/$', 'logout'),
)

urlpatterns += staticfiles_urlpatterns()