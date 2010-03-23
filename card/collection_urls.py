from django.conf.urls.defaults import *


from models import Card, Collection

collection_dict = {'queryset': Collection.objects.all()}
urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', collection_dict), # list of collections
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', collection_dict, 'collection_details'), #details on a single collection
                       (r'^(?P<collection_id>\d+)/edit/$', 'card.views.collection_edit'), #submit edit
                       (r'^(?P<collection_id>\d+)/quiz$', 'django.views.generic.list_detail.object_detail',
                        dict(queryset=collection.objects.all(),
                             template_name="card/collection_quiz.html")), #quiz for single card
                       
                       (r'^(?P<collection_id>\d+)/answer$', 'django.views.generic.list_detail.object_detail', 
                        dict(queryset=Card.objects.all(),
                             template_name="card/card_answer.html")), #answer for single card
)
