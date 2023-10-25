from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic
from django.shortcuts import redirect
from tasks.forms import TaskForm
from tasks.models import Task, Tag


class IndexView(View):
    template_name = "tasks/index.html"

    def get(self, request):
        tasks = Task.objects.all()
        tags = Tag.objects.all()
        context = {
            "task": tasks,
            "tag": tags,
        }
        return render(request, self.template_name, context=context)


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:index")


def toggle_task(request, task_id):
    if request.method == "POST" and "toggle" in request.POST:
        task = Task.objects.get(pk=task_id)
        task.is_completed = not task.is_completed
        task.save()

    return redirect("tasks:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tags.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tag")
