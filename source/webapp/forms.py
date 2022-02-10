from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import IssueTracker, Project


class IssueTrackerForm(forms.ModelForm):
    class Meta:
        model = IssueTracker
        exclude = []
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 30}),
            'type': forms.CheckboxSelectMultiple()
        }

    def clean(self):
        cleaned_data = super().clean()
        summary = cleaned_data['summary']
        description = cleaned_data['description']
        if len(summary) < 5:
            self.add_error('summary', ValidationError(
                f"Значение должно быть длиннее 5 символов {summary} не подходит"))
        if summary == description:
            raise ValidationError("Text of the tasks should not duplicate it's title!")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description")


class IssueTrackerDeleteForm(forms.ModelForm):
    class Meta:
        model = IssueTracker
        fields = ("summary",)

    def clean_title(self):
        if self.instance.summary != self.cleaned_data.get("summary"):
            raise ValidationError("Название не соответствует")
        return self.cleaned_data.get("summary")

