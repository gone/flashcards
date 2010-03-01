# Create your views here.
from models import Card, Collection
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def submit_edit(request, card_id):
	""" save edits to a card"""
	card = get_object_or_404(Card, pk=card_id)
	card.question = request.POST['question'].strip()
	card.answer = request.POST['answer'].strip()
	card.save()
	return HttpResponseRedirect(reverse('card_details', args=(card_id, )))

def answer(request, card_id):
	pass

def card_manage_collections(request, card_id):
	collections = Collection.objects.all()
	card = Card.objects.get(pk=card_id)
	for collection in collections:
		if card in collection.cards.all():
			collection.in_card = True
		else:
			collection.in_card = False
	ctx = RequestContext(request, {'card':card, 'collections':collections})
	return render_to_response('card/card_manage_collection.html', ctx)