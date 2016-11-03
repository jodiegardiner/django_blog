# from django import *
from django.conf.urls import url, include
from django.contrib import admin
from settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^blog/', include('blog.urls')),
]
