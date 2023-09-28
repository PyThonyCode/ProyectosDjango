from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import TaskForm, ProjectForm

# Create your views here.


def index(request):
    title = 'Django Course!!!'
    return render(request, 'index.html', {
        'titulo': title
    })


def hello(request, username, edad):
    result = edad*3
    return HttpResponse("<h1>HOLA MUNDO %s</h1>" % result)


def about(request):
    return render(request, 'about.html')


"""def projects(request):
    p = list(Project.objects.values())
    print(p)
    return JsonResponse(p, safe=False)"""


"""def projects(request):
    p = list(Project.objects.values())
    return render(request, 'projects.html')"""


def projects(request):
    p = Project.objects.all()
    return render(request, 'project/projects.html', {
        'project': p
    })


"""def tasks(request, title):
    t = Task.objects.get(title=title)
    return HttpResponse('Tasks: %s' % t.id)"""


def tasks(request):
    t = Task.objects.all()
    return render(request, 'task/tasks.html', {
        'task': t
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'task/create_task.html', {
            'form': TaskForm()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {
            'form': ProjectForm()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'project/project_detail.html', {
        'project': project,
        'tasks': tasks
    })
