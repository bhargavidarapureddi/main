from django.shortcuts import render
from studentApp import forms

# Create your views here.
def studentinputview(request):
    # form=forms.StudentForm()
    # my_dict={'form':form}
    # return render(request,'input.html',context=my_dict)
    form=forms.StudentForm()
    if request.method=='POST':
       form=forms.StudentForm(request.POST)
    if form.is_valid():
        print("Form validation success and printing data")
        print("'Name:",form.cleaned_data['name'])
        print("Marks:",form.cleaned_data['marks'])
    return render(request,'input.html',{'form':form})   