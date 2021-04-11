"""aps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from webapp import views as webapp_views
from toDoList import views as to_do_list_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp_views.index_view, name='index'),
    path('index1', webapp_views.index1_view),
    path('articles/add/', webapp_views.article_create_view, name='article_add'),
    path('article/<int:pk>', webapp_views.article_view, name='article_view'),
    path('calc_form/add/', webapp_views.calc_form_view),
    path('task/', to_do_list_views.task, name='task'),
    path('task/<int:pk>/', to_do_list_views.task_view, name='task_view'),
    path('task/add/', to_do_list_views.task_create_view, name='task_add'),
    path('task/<int:pk>/delete/', to_do_list_views.task_delete, name='task_delete'),
    path('task/<int:pk>/edit/', to_do_list_views.task_update, name='task_update'),
    path('article/<int:pk>/edit/', webapp_views.article_update_view, name='article_update'),
    path('article/<int:pk>/delete/', webapp_views.article_delete_view, name='article_delete')
]
