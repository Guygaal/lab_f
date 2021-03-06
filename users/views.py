from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Завершает сеанс работы с приложением."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


# Create your views here.

def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            return render(request, 'learning_logs/proof.html')
    context = {'form': form}
    return render(request, 'users/register.html', context)
