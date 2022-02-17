from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.forms import ProjectForm
from webapp.models import Project, IssueTracker


class ProjectCreateView(PermissionRequiredMixin,CreateView):
    model = Project
    template_name = 'tasks/create.html'
    form_class = ProjectForm
    permission_required = "webapp.add_project"

    def form_valid(self, form):
        task = get_object_or_404(IssueTracker, pk=self.kwargs.get('pk'))
        project = form.save(commit=False)
        project.author = self.request.user
        project.task = task
        project.save()
        return redirect('webapp:task_view', pk=task.pk)


class ProjectUpdateView(PermissionRequiredMixin,UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectForm
    permission_required = "webapp.change_project"

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:task_view", kwargs={"pk": self.object.task.pk})


class ProjectDeleteView(PermissionRequiredMixin,DeleteView):
    model = Project
    permission_required = "webapp.delete_project"

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:task_view", kwargs={"pk": self.object.task.pk})
