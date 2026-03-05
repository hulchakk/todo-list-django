from django.views import generic

from todo_app.models import (
    Task,
    Tag,
)


class TaskListView(generic.ListView):
    model = Task
