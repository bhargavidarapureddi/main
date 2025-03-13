from django.shortcuts import render
from productApp import forms

# Create your views here.
def product_view(request):
    form=forms.ProductForm()
    if request.method=='POST':
        form=forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'input.html',{'form':form})