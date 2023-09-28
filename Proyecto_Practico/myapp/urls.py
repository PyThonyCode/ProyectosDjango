from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/<str:username>/<int:edad>', views.hello),
    path('about/', views.about),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    # path('tasks/<str:title>', views.tasks)
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project')
]
