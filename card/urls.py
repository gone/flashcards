from django.conf.urls.defaults import *


from models import Card, Collection

collection_dict = {'queryset': Collection.objects.all()}
card_dict = {'queryset': Card.objects.all()}
urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', card_dict), # list of cards
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', card_dict, 'card_details'), #details on a single card
                       (r'^(?P<card_id>\d+)/edit/submit/$', 'card.views.submit_edit'), #submit edit
                       (r'^(?P<card_id>\d+)/collections/', 'card.views.card_manage_collections'),
                       (r'^(?P<card_id>\d+)/collections/submit', 'card.views.submit_card_manage_collections'),
                       (r'^(?P<object_id>\d+)/edit/$', 'django.views.generic.list_detail.object_detail',
                        dict(queryset=Card.objects.all(),
                             template_name="card/card_edit.html")), #edit single card

                       (r'^(?P<object_id>\d+)/quiz$', 'django.views.generic.list_detail.object_detail',
                        dict(queryset=Card.objects.all(),
                             template_name="card/card_quiz.html")), #quiz for single card
                       
                       (r'^(?P<object_id>\d+)/answer$', 'django.views.generic.list_detail.object_detail', 
                        dict(queryset=Card.objects.all(),
                             extra_context={"range":xrange(6)},
                             template_name="card/card_answer.html")), #answer for single card
)
