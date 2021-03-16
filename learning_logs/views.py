from django.shortcuts import render
from .models import Topic, Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm, EntryReadForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.db.models import Q


def index(request):
    return render(request, 'learning_logs/index.html')


def waiting_room(request):
    return render(request, 'learning_logs/proof')


@login_required
def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.order_by('date_added')
    """.filter(owner=request.user)"""
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Выводит одну тему и все ее записи."""
    topic = Topic.objects.get(id=topic_id)
    # if topic.owner != request.user:
    #    raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


# Create your views here.


@login_required
def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.name = Entry.objects.count()
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #if entry.owner != request.user:
    #   raise Http404
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать данные.
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def read_entry(request, entry_id):
    """Читает существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # if topic.owner != request.user:
    #    raise Http404
    # Исходный запрос; форма заполняется данными текущей записи.
    form = EntryReadForm(instance=entry)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/read_entry.html', context)


@login_required
def entry_search(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    query = request.GET.get('q')
    query.lower()
    query = query.replace('мпгу', 'MSUE')
    query = query.replace('мфти', 'MIPT')
    query = query.replace('ирэ', 'IRE')
    query = query.replace('другое', 'OTHER')

    entries = topic.entry_set.filter(Q(name__icontains=query) |
                                     Q(text__icontains=query) |
                                     Q(microch__icontains=query) |
                                     Q(micro_adv__icontains=query) |
                                     Q(resist__icontains=query) |
                                     Q(tr_rec__icontains=query) |
                                     Q(owner__username__icontains=query) |
                                     Q(owner__first_name__icontains=query) |
                                     Q(owner__last_name__icontains=query))
    entries = entries.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
