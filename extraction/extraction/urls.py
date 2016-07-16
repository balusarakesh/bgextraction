from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'extraction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^bgextr/', include('bgextr.urls', namespace='bgextr')),
    url(r'^admin/', include(admin.site.urls))
    ) 
