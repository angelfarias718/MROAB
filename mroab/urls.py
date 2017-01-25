from django.conf.urls import include, url, patterns
from django.contrib import admin
from mroab_app import views
urlpatterns = patterns('',
    url(r'^$', include('mroab_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site/(?P<slug>[-\w]+)/$', 'mroab_app.views.site'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
)