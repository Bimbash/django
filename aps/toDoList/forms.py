from django import forms
from django.forms import widgets

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Задача')
    text = forms.CharField(max_length=3000, required=True, label='Описание', widget=widgets.Textarea)
    check = forms.ChoiceField(required=True, choices=status_choices, widget=widgets.Select, label='Статус')
    date = forms.DateField(required=True, label='Дата выполнения')

    # title = forms.CharField(max_length=200, required=True, label='Title')
    # author = forms.CharField(max_length=40, required=True, label='Author')
    # text = forms.CharField(max_length=3000, required=True, label='Text', widget=widgets.Textarea)