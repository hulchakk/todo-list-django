from django.urls import path

from todo_app.views import (
    TaskListView,
    TaskCreateView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="todo-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]


app_name = "todo_app"
