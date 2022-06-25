from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetails(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
# Create your views here.

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('to-do-list')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('to-do-list')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('to-do-list')
