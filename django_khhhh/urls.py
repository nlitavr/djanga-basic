from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import hello_template

urlpatterns = patterns('',	
	# Set home page
	url(r'^$', 'django_khhhh.views.home'),

	# Procedural calls
	url(r'^hello/$', 'article.views.hello'),
	url(r'^hello_template/$', 'article.views.hello_template'),

	# Simple Way
	url(r'^hello_temp/$', 'article.views.hello_temp'),

	# Simplest Way
	url(r'^hi_t/$', 'article.views.hi_t'),


	# Class based call
	url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
	url(r'^hello_class_view/$', hello_template.as_view()),

	# Whenever 'articles/' is typed	=> map that through to the set of urls from article.urls
	# (r'^articles$/', include('article.urls')),	
    # Examples:
    # url(r'^$', 'django_khhhh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
