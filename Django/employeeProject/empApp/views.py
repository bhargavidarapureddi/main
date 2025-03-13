from django.shortcuts import render
from empApp.models import Employee
 
# Create your views here.
def empData(request):
    empData={"empno":101,"ename":"chinni","sal":4000}
    return render(request,'emp.html',context=empData)

def empDB(request):
    data=Employee.objects.all()
    my_dict={'emplist':data}
    return render(request,'emplist.html',context=my_dict)