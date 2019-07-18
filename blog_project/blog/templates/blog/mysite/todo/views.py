from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from .models import TodoData
from .forms import TodoDataForm
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class OwnObjectsMixin():
    """
    Only returns objects that belongs to the current user. Assumes the object
    has a 'user' foreignkey to a User.
    """
    def get_queryset(self):
        author = self.request.user
        return super(OwnObjectsMixin, self).get_queryset().filter(author=author)

class TodoList(LoginRequiredMixin,OwnObjectsMixin,ListView):
    model = TodoData
    template_name ='todo/index.html'
    context_object_name = 'todo_list'

class TodoCreate(LoginRequiredMixin,CreateView):
    model = TodoData
    form_class = TodoDataForm
    template_name = 'todo/addtodo.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TodoCreate, self).form_valid(form)


class TodoUpdate(LoginRequiredMixin,UpdateView):
    model = TodoData
    form_class = TodoDataForm
    template_name = 'todo/updatetodo.html'
    success_url = reverse_lazy('homepage')

class TodoDelete(LoginRequiredMixin,DeleteView):
    model = TodoData
    template_name = 'todo/deletetodo.html'
    success_url = reverse_lazy('homepage')
