from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^tasks/(?P<task_id>\d+)/$', views.task, name='task'),
    #Страница для добавления новой темы
    url(r'^new_task/$', views.new_task, name='new_task'),
    #Страница для редактирования записи
    url(r'^edit_task/(?P<task_id>\d+)/$', views.edit_task, name='edit_task'),
]