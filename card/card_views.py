# Create your views here.
from models import Card, Collection
from forms import CollectionForm, CardForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

def start_quiz(request, set_id):
	pass

def update_hand(current_hand, larger_set, confidence, current_item):
	pass
	# """updates current_hand after a confidence level is given
	# NOTES: this mutates both larger_set and current_hand"""
	# position = 0 #replace this with new position
	# if position = 0:
	# 	current_item = larger_set.pop()
	# 	position = -1
	# current_hand = current_hand[0:position] + [current_item] + current_hand[position:]
	# return current_hand
	
# def manage_collections(request, card_id):
# 	collections = Collection.objects.filter(cardsa)
# 	card = Card.objects.get(pk=card_id)
# 	frm = CardForm()
# 	ctx = RequestContext(request, {'card':card, 'form':frm})
# 	return render_to_response('card/card_manage_collection.html', ctx)
