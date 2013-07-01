from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('zivotopis.views',
    url(r'^unos/$', 'cv_add', name='cv_add'),
    url(r'^(?P<cv_id>\d+)/$', 'cv_detail', name='cv_detail'),
    url(r'^pregled/$', 'cv_list', name='cv_list'),
)
