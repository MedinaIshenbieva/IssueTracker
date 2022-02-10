from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ProjectForm
from webapp.models import Project, IssueTracker


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'tasks/create.html'
    form_class = ProjectForm

    def form_valid(self, form):
        task = get_object_or_404(IssueTracker, pk=self.kwargs.get('pk'))
        project = form.save(commit=False)
        project.task = task
        project.save()
        return redirect('webapp:task_view', pk=task.pk)


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("webapp:task_view", kwargs={"pk": self.object.task.pk})


class ProjectDeleteView(DeleteView):
    model = Project

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:task_view", kwargs={"pk": self.object.task.pk})

