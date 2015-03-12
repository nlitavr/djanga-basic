from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView

# Create your views here.
def hello(request):
	name = "Kolyan"
	html = "<html><body> %s znaet trapinki volwebnix polyan!</body></html>" % name
	return HttpResponse(html)

def hello_temp(request):
	name = "Kolyan"
	t = get_template('hello.html')
	html = t.render(Context({'name': name}))	
	return HttpResponse(html)

def hi_t(req):
	name = "K"
	return render_to_response('hello.html', {'name' : name})

class hello_template(TemplateView):
	template_name = 'hello_class.html'

	def get_context_data(self, **kwargs):
		context = super(hello_template, self).get_context_data(**kwargs)
		context['name']	= 'Kolyan'
		return context
	# t = get_template('hello.html')
	# html = t.render(Context({'name' : name}))
	# return HttpResponse(html)