from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',    
    url(r'^$', 'website.views.home'),
	#additions
	url(r'^createPage/$', 'website.views.createPage'),
	url(r'^addrow/(?P<page_id>\d+)/$', 'website.views.addRow'),
	url(r'^addcol/(?P<row_id>\d+)/$', 'website.views.addCol'),
	url(r'^addCode/(?P<column_id>\d+)/$', 'website.views.addCode'),
	
	#temporary
	url(r'^addCode2/(?P<column_id>\d+)/$', 'website.views.addCode2'),
	
	#deletions
	url(r'^delrow/(?P<row_id>\d+)/$', 'website.views.deleteRow'),
	url(r'^delcol/(?P<column_id>\d+)/$', 'website.views.deleteCol'),
	url(r'^delCode/(?P<column_id>\d+)/$', 'website.views.delCode'),
	
	#reset
	url(r'^reset/$', 'website.views.reset'),
	
    url(r'^admin/', include(admin.site.urls)),
)
