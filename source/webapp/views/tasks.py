from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import IssueTrackerForm, IssueTrackerDeleteForm
from webapp.models import IssueTracker
from webapp.views.base import SearchView


class IndexView(SearchView):
    model = IssueTracker
    context_object_name = "tasks"
    template_name = "tasks/index.html"
    paginate_by = 3
    paginate_orphans = 0
    search_fields = ["summary__icontains", "descriptions__icontains"]
    ordering=["-updated_at"]


class IssueTrackerCreateView(LoginRequiredMixin, CreateView):
    model = IssueTracker
    form_class = IssueTrackerForm
    template_name = "tasks/create.html"


class IssueTrackerView(DetailView):
    template_name = 'tasks/view.html'
    model = IssueTracker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        summary = self.object.comments.order_by("-created_at")
        context['summary'] = summary
        return context


class IssueTrackerUpdateView(UpdateView):
    form_class = IssueTrackerForm
    template_name = "tasks/update.html"
    model = IssueTracker


class IssueTrackerDeleteView(DeleteView):
    model = IssueTracker
    template_name = "tasks/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = IssueTrackerDeleteForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs['instance'] = self.object
        return kwargs