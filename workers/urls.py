from django.conf.urls import url

from . import views

urlpatterns = [
    #Домашняя страница
    url(r'^emps/$', views.emps, name='emps'),
    url(r'^emps/(?P<emp_id>\d+)/$', views.emp, name='emp'),
    #Страница для добавления новой темы
    url(r'^new_emp/$', views.new_emp, name='new_emp'),
    #Для добавления проектов
    url(r'^add_tasks/(?P<emp_id>\d+)/$', views.add_tasks, name='add_tasks'),
    #Страница для редактирования записи
    url(r'^edit_emp/(?P<emp_id>\d+)/$', views.edit_emp, name='edit_emp'),
]