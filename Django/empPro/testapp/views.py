from django.shortcuts import render,redirect 
from testapp.forms import EmployeeForm 
from testapp.models import Employee 

# Create your views here. 
def show_view(request): 
    employees=Employee.objects.all()
    return render(request,'index.html',{'employees':employees}) 

def insert_view(request): 
    form=EmployeeForm()
    if request.method=='POST': 
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('/') 
    return render(request,'insert.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/') 

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/') 
    return render(request,'update.html',{'employee':employee})