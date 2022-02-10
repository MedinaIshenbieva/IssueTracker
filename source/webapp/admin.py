from django.contrib import admin

# Register your models here.
from webapp.models import IssueTracker, Status, Type, Project


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['status', 'type']
    fields = ['summary', 'description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(IssueTracker)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
