"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appdabia import views

urlpatterns = [
    path('', views.home,name='home'),
    path('admin/', admin.site.urls),
    path('tasks/', views.list_tasks),
    path('tasks/create/', views.create_task),
    path('programa', views.create_programas),
    path('programa/update/<id>', views.update_programas),
    path('programa/delete/<id>', views.delete_programas),
    path('trilha', views.create_trilhas),
    path('trilha/update/<id>', views.update_trilhas),
    path('trilha/delete/<id>', views.delete_trilhas),
]


