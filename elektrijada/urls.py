from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^zivotopisi/', include('zivotopis.urls', namespace='zivotopis', app_name='zivotopis')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^korisnici/prijava/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^korisnici/odjava/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)

# staticfiles_urlpatterns() returns only if DEBUG, static also
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
