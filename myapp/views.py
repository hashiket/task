from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def index(request):
    return render(request,"myapp/main.html")


def addtask(request):
    if request.method == 'POST':
        name = request.POST['name']
        Task.objects.create(name=name)
        return redirect('/')
    else:
        return render(request,"myapp/addtask.html")

def alltask(request):
    tasks = Task.objects.all()
    return render(request,"myapp/alltask.html",{'tasks':tasks})


def task(request,id):
    task = Task.objects.get(id=id)
    return render(request,"myapp/task.html",{'task':task})

def comtask(request):
    tasks = Task.objects.filter(status=True)
    return render(request,"myapp/comptask.html",{'tasks':tasks})

def pentask(request):
    tasks = Task.objects.filter(status=False)
    return render(request,"myapp/pentask.html",{'tasks':tasks})

def delete(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return render(request,"myapp/alltask.html")

def complete(request,id):
    task = Task.objects.get(id=id)
    task.status = True
    task.save()
    return render(request,"myapp/task.html",{'task':task})
