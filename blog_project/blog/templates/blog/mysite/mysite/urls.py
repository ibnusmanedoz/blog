"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from todo.views import TodoList, TodoCreate, TodoUpdate, TodoDelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TodoList.as_view(), name='homepage'),
    path('todo/add/',TodoCreate.as_view(), name = 'todo-add'),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('todo/<int:pk>/update/',TodoUpdate.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/',TodoDelete.as_view(), name = 'todo-delete'),

]
