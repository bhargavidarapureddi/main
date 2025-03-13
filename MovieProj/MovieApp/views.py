from django.shortcuts import render 
from MovieApp.forms import MovieForm 
from MovieApp.models import Movie 

# Create your views here. 

def index_view(request): 
	return render(request,'index.html') 
 
def add_movie_view(request): 
	form=MovieForm() 
	if request.method=='POST': 
		form=MovieForm(request.POST) 
		if form.is_valid(): 
			form.save() 
		return index_view(request) 
	return render(request,'addmovie.html',{'form':form}) 
 
def list_movie_view(request):
	movies_list=Movie.objects.all().order_by('-rating') 
	return render(request,'listmovie.html',{'movies_list':movies_list})