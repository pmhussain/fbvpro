from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def read(request):
    employees = Employee.objects.all()
    return render(request,"testApp/home.html",{'employees':employees})

def create(request):
    form=EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"testApp/create.html",{'form':form})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form=EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"testApp/update.html",{'form':form})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    # employee.delete()
    # return redirect('/')
    if request.method == 'POST':
        if request.POST['response']=='YES':
            employee.delete()
            return redirect('/')
        elif request.POST['response']=='NO':
            return redirect('/')
    return render(request,"testApp/delete.html",{'employee':employee})
