from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from toDoList.forms import TaskForm
from toDoList.models import Task


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('task')


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={
            'title': task.title,
            'text': task.text,
            'check': task.check,
            'date': task.date
        })
        return render(request, 'task_update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.check = form.cleaned_data['check']
            task.text = form.cleaned_data['text']
            task.date = form.cleaned_data['date']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                check=form.cleaned_data['check'],
                date=form.cleaned_data['date']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})


def task_view(request, pk):
    task = get_object_or_404(Task,pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def task(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task.html', context)
