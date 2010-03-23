from django.db import models
from datetime import datetime
import tagging, tagging.fields

# Create your models here.

class Card(models.Model):
	title = models.CharField(max_length=100)
	question = models.TextField()
	answer = models.TextField()
	pub_date = models.DateTimeField('date published', default=datetime.now())
	tgs = tagging.fields.TagField()
	def get_absolute_url(self):
		return "/cards/%s/" % self.id
	def __unicode__(self):
		return self.title

class Collection(models.Model):
	title = models.CharField(max_length=100)
	cards = models.ManyToManyField(Card, blank=True, related_name="collections")
	def __unicode__(self):
		return self.title
	def get_cards(self):
		c = Collection.objects.get(id=self.id)
		cards = c.cards.all()
		return list(cards)
	def get_absolute_url(self):
		return "/collections/%s/" % self.id
		
# class CardSet(models.Model):
# 	title = models.CharField(max_length=100)
# 	Collections = models.ManyToManyField(Card, blank=True, related_name="")
# 	def __unicode__(self):
# 		return self.title
# 	def get_collections(self):
# 		s = CardSet.objects.get(id=self.id)
# 		c = s.collections.all()
# 		return list(c)
# 	def get_cards(self):
# 		cols = self.get_collections()
# 		c = [col.get_cards() for col in cols]
# 		return merge(c)

def merge(thelist):
	rv = []
	for alist in thelist:
		rv.extend(alist)
	return rv
		
