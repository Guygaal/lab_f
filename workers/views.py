from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Emp
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EmpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

@login_required
def emps(request):
    """Выводит список тем."""
    emps = Emp.objects.order_by('date_added')
    """.filter(owner=request.user)"""
    context = {'emps': emps}
    return render(request, 'workers/emps.html', context)


@login_required
def emp(request, emp_id):
    """Выводит один проект."""
    emp = Emp.objects.get(id=emp_id)
    # if emp.owner != request.user:
    #    raise Http404
    #emps = emp.emp_set.order_by('-date_added')
    context = {'emp': emp}
    return render(request, 'workers/emp.html', context)


@login_required
def new_emp(request):
    """Определяет новый проект."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EmpForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EmpForm(request.POST)
        if form.is_valid():
            new_emp = form.save(commit=False)
            new_emp.owner = request.user
            new_emp.save()
            return HttpResponseRedirect(reverse('workers:emps'))
    context = {'form': form}
    return render(request, 'workers/new_emp.html', context)


@login_required
def edit_emp(request, emp_id):
    """Редактирует существующий проект."""
    emp = Emp.objects.get(id=emp_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EmpForm(instance=emp)
    else:
        # Отправка данных POST; обработать данные.
        form = EmpForm(request.POST, request.FILES, instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('workers:emp',
                                                args=[emp.id]))
    context = {'emp': emp, 'form': form}
    return render(request, 'workers/edit_emp.html', context)