from django import forms

from todo_app.models import (
    Task,
    Tag,
)


class TaskForm(forms.ModelForm):
    datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            }
        )
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            }
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "datetime",
            "deadline",
            "tags",
        )
