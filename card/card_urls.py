from django.conf.urls.defaults import *


from models import Card, Collection

collection_dict = {'queryset': Collection.objects.all()}
card_dict = {'queryset': Card.objects.all()}
urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', card_dict), # list of cards
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', card_dict, 'card_details'), #details on a single card
					   (r'^new/$', 'django.views.generic.create_update.create_object', {"model": Card}), #details on a single card
                       (r'^edit/(?P<object_id>\d+)/$', 'django.views.generic.create_update.update_object', {"model": Card}), 
					   (r'^remove/(?P<object_id>\d+)/$', 'django.views.generic.create_update.delete_object', {"model": Card,
																											"post_delete_redirect" : "/cards/"}), 
#                       (r'^collections/(?P<card_id>\d+)/$', 'card.card_views.manage_collections'), #check which collections hold this card
                       (r'^quiz/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', {'queryset': Card.objects.all(),
																										'template_name': 'card_quiz.html',},
																										'card_details'),
)
					   
