from django.conf.urls import patterns, url

urlpatterns = patterns(
    'rates.views',
    url(r'^$', 'new_deal', name='new_deal'),
)
