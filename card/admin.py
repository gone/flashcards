from models import Card, Collection
from django.contrib import admin


class CardAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['question', 'answer']}),
		(None, {'fields':['tgs']}),
		('Date Information', {'fields':['pub_date'], 'classes' : ['collapse']}),
		]
	date_herarchy = 'pub_date'

admin.site.register(Card, CardAdmin)
admin.site.register(Collection)
