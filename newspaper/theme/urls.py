from django.conf.urls import patterns, url

urlpatterns = patterns(
    'theme.views',
    url(r'^$', 'base', name='base'),
)