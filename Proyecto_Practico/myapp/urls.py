from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hello),
    path('about/', views.about)
]