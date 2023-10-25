from django.urls import path
from tasks.views import (
    TaskListView,
    TagListView,
    TaskUpdateView,
    TagUpdateView,
    TaskDeleteView,
    TagDeleteView,
    TagCreateView,
    TaskCreateView, ToggleTaskView,
)
from . import views

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="create-task"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task"),
    path("toggle-task/<int:task_id>/", ToggleTaskView.as_view(), name="toggle-task"),
    path("tags/", TagListView.as_view(), name="tag"),
    path("tags/create/", TagCreateView.as_view(), name="create-tag"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="update-tag"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="delete-tag"),
]

app_name = "tasks"
