from django.contrib import admin
from toDoList.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'check', 'date']
    list_filter = ['title']
    search_fields = ['title', 'text']
    fields = ['title', 'text', 'check', 'date']


admin.site.register(Task, TaskAdmin)
