
from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from .models import Todo as TodoModel

class TodoListView(ListView):
    model = TodoModel
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

class TodoCreateView(CreateView):
    model = TodoModel
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = TodoModel
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = TodoModel
    success_url = reverse_lazy('todo_list')
