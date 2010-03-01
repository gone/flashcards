from django.db import models
from datetime import datetime
import tagging, tagging.fields

# Create your models here.


class Card(models.Model):
	question = models.TextField()
	answer = models.TextField()
	pub_date = models.DateTimeField('date published', default=datetime.now())
	tgs = tagging.fields.TagField()
	#something about who published it
	def __unicode__(self):
		return self.question

class Collection(models.Model):
	title = models.CharField(max_length=100)
	cards = models.ManyToManyField(Card)
	def __unicode__(self):
		return self.title
