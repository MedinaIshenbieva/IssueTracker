from django.urls import path
from django.views.generic import RedirectView

from webapp.views import(
    IndexView,
    IssueTrackerCreateView,
    IssueTrackerView,
    IssueTrackerUpdateView,
    IssueTrackerDeleteView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('tasks/', RedirectView.as_view(pattern_name="index")),
    path('tasks/add/', IssueTrackerCreateView.as_view(), name="task_add"),
    path('task/<int:pk>/', IssueTrackerView.as_view(template_name="tasks/view.html"), name="task_view"),
    path('task/<int:pk>/update/', IssueTrackerUpdateView.as_view(), name="task_update_view"),
    path('task/<int:pk>/delete/', IssueTrackerDeleteView.as_view(), name="task_delete_view"),
    path('task/<int:pk>/projects/add/', ProjectCreateView.as_view(), name="task_project_create"),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name="project_update_view"),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name="project_delete_view"),
]
