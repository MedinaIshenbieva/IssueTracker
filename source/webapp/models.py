from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
from django.urls import reverse


class IssueTracker(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name="Краткое описание",
                               validators=(MinLengthValidator(10),))
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT,
                               related_name='status', verbose_name="Статус")
    type = models.ManyToManyField('webapp.Type', related_name='type', blank=True, verbose_name="Тип")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    project = models.ForeignKey('webapp.Project',
                                on_delete=models.CASCADE,
                                related_name='project',
                                verbose_name="Проект",
                                null=True,
                                default=1)

    def get_absolute_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.pk})

    def upper(self):
        return self.summary.upper()

    def __str__(self):
        return f"{self.pk}. {self.summary}" \
                f"{self.type}," \
                f"{self.status}."

        class Meta:
            db_table = 'tasks'
            verbose_name = 'Задача'
            verbose_name_plural = 'Задачи'


class Status(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Project(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name="Название")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    start_time = models.DateField(blank=True, verbose_name="Дата начала")
    finish_time = models.DateField(null=True, verbose_name="Дата окончания")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'