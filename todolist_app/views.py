from asyncio import all_tasks
from re import M
from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages

# Create your views here.

def todolist(request):
    if request.method=='POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('New Task Added'))
        return redirect('todolist')
    else:
        all_tasks=TaskList.objects.all
        return render(request,'todolist.html',{'all_tasks':all_tasks})

def contact(request):
    context={
        'contact_text':"'Welcome Contact"
    }
    return render(request,'contact.html',context)

def about(request):
    context={
        'about_text':"'Welcome About"
    }
    return render(request,'about.html',context)
