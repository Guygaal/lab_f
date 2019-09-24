from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.db.models import Q

@login_required
def tasks(request):
    """Выводит список тем."""
    tasks = Task.objects.order_by('date_added')
    """.filter(owner=request.user)"""
    context = {'tasks': tasks}
    return render(request, 'projects/tasks.html', context)


@login_required
def task(request, task_id):
    """Выводит один проект."""
    task = Task.objects.get(id=task_id)
    # if task.owner != request.user:
    #    raise Http404
   # entries = task.entry_set.order_by('-date_added')
    context = {'task': task}
    ''', 'entries': entries}'''
    return render(request, 'projects/task.html', context)


@login_required
def new_task(request):
    """Определяет новый проект."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TaskForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return HttpResponseRedirect(reverse('projects:tasks'))
    context = {'form': form}
    return render(request, 'projects/new_task.html', context)


@login_required
def edit_task(request, entry_id):
    """Редактирует существующий проект."""
    entry = task.objects.get(id=entry_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = TaskForm(instance=task)
    else:
        # Отправка данных POST; обработать данные.
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects:task',
                                                args=[task.id]))
    context = {'task': task, 'form': form}
    return render(request, 'projects/edit_task.html', context)