from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.http import HttpResponse 
from testapp.models import Book  
 
# Create your views here. 
class HelloWorldView(View): 
	def get(self,request): 
		return HttpResponse('<h1>This is from ClassBasedView</h1>')
class TemplateCBV(TemplateView):
	template_name = 'home.html'
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = 'BlueYonder'
		context['age'] = 30
		return context

# Create your views here. 
class BookListView(ListView): 
	model=Book