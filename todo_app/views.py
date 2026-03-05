from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import (
    Task,
    Tag,
)


def task_change_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done

    task.save()

    return redirect("todo_app:todo-list")


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:todo-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:todo_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:todo-list")
