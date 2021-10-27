from django.http import request
from enroll.models import Student
from django.shortcuts import redirect, render
from .forms import StudentRegister
from django.contrib import messages

def add_show(request):
    if request.method == "POST":
        form = StudentRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student details added.')
            return redirect('/')
    else:
        form = StudentRegister()

    stud = Student.objects.all()
    return render(request, 'addandshow.html', {'form':form, 'stud':stud})

def delt(request, id):
    stud = Student.objects.get(id = id)
    stud.delete()
    messages.warning(request, 'Student details deleted.')
    return redirect('/')
    
def edt(request, id):
    stud = Student.objects.get(id=id)
    editstud = StudentRegister(instance=stud)
    if request.method == "POST":
        form = StudentRegister(request.POST, instance=stud)
        if form.is_valid():
            form.save()
            messages.success(request, 'student details updated succesfully !')
            return redirect('/')

    return render(request, "update.html", {'editstud':editstud})

    

