from django.shortcuts import render 
from companyapp.models import Company 
from django.urls import reverse_lazy 
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView 

# Create your views here. 
class CompanyListView(ListView): 
	model=Company 
	#default template_name is company_list.html 
	#defult context_object_name is company_list
 
class CompanyDetailView(DetailView):
	model=Company 
	#default template_name is company_detail.html 
	#defult context_object_name is company or object

class CompanyCreateView(CreateView):
	model=Company
	fields=('name','location','ceo')

class CompanyUpdateView(UpdateView): 
	model=Company 
	fields=('name','location','ceo')
	success_url=reverse_lazy('companies')

class CompanyDeleteView(DeleteView):
	model=Company
	success_url=reverse_lazy('companies') 