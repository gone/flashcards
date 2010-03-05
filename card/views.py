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

def edit(request, card_id):
	""" save edits to a card"""
	card = get_object_or_404(Card, pk=card_id)
	if request.method == "POST":
		#submission
		cf = CardForm(request.POST, instance=card)
		if cf.is_valid():
			card.question = cf.cleaned_data['question']
			card.answer   = cf.cleaned_data['answer']
			card.pub_date = cf.cleaned_data['pub_date']
			tgs = cf.cleaned_data['tgs']
			card.save()
			return HttpResponseRedirect(reverse('card_details', args=(card_id, )))
	else:
		cf = CardForm(instance=card)

	ctx = RequestContext(request, {'card':cf})
	return render_to_response("card/card_edit.html", ctx)

def start_quiz(request, set_id):
	pass

def quiz(request, card_id):
	if not request.session['set']:
		return HttpResponseRedirect(reverse('quiz_complete'))
	card = get_object_or_404(Card, pk=card_id)
	if request.method == "POST":
		messages.success(request, "this is a test of the emergency broadcasting system")
		how_sure = request.POST['Submit']
		current_card = hand.pop()
		update_hand(request.session['hand'], request.session['set'], how_sure, current_card)
		card = request.session['hand'][0]
	ctx = RequestContext(request, {"card":card})
	return render_to_response("card/card_quiz.html", ctx)

	
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
	
def card_manage_collections(request, card_id):
	collections = Collection.objects.all()
	card = Card.objects.get(pk=card_id)
	f = CollectionForm()
	ctx = RequestContext(request, {'card':card, 'collection':f})
	return render_to_response('card/card_manage_collection.html', ctx)

