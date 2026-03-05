from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import (
    Task,
    Tag,
)


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:todo-list")
