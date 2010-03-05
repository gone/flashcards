from django.conf.urls.defaults import *
from django.views.generic import simple as simple
from django.contrib.auth import urls as auth_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^flashcard/', include('flashcard.card.urls')),
    (r'^cards/', include('flashcard.card.card_urls')),
    (r'^auth/', include(auth_urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', simple.direct_to_template, {'template':'index.html'}),
)
