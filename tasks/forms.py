from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    dead_line = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Optional: You can specify a deadline date if needed."
            }
        ),
        help_text="Enter the deadline date as you wish (e.g., YYYY-MM-DD HH:MM)",
    )

    class Meta:
        model = Task
        fields = ["title", "dead_line", "is_completed", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
        }
