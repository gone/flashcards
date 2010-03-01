from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()

@register.filter
def times(count):
    return xrange(int(count))

@register.filter
def evalfunc(func, args):
	if args:
		print func
		print args
		args = str(args).split()
		print "%s(*%s)" % (func, args)
		return eval("%s(*%s)" % (func, args))
	else:
		return eval("%s()" % func)
