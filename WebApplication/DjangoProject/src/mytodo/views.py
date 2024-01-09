
# Create your views here.

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mytodo.models import Task

class TaskListView(ListView):
    model = Task
    template_name = "mytodo/list.html"

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    initial = {'status':0}
    template_name = 'mytodo/create.html'
    success_url = reverse_lazy('mytodo:task-list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'mytodo/detail.html'

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'mytodo/update.html'
    success_url = reverse_lazy('mytodo:task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'mytodo/delete.html'
    success_url = reverse_lazy('mytodo:task-list')
