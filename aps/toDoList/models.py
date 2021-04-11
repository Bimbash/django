from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Задача')
    text = models.TextField(max_length=3000, null=False, blank=True, verbose_name='Описание')
    check = models.CharField(max_length=100, null=False, blank=True, choices=status_choices, default='new', verbose_name='Статус')
    date = models.DateField(default='', verbose_name='Дата выполнения')


def __str__(self):
    return "{}. {}".format(self.pk, self.title)


