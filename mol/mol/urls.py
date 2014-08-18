from django.conf.urls import patterns, include, url

from django.contrib import admin
from compounds import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^cas/',include('cas.urls', namespace='cas')),
)
