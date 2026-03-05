from django.urls import path

from todo_app.views import (
    TaskListView,
    TaskCreateView,
    task_change_status,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="todo-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/change_status",
        task_change_status,
        name="task-change-status"
    )
]


app_name = "todo_app"
