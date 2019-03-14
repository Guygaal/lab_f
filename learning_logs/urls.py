from django.conf.urls import url

from . import views
urlpatterns = [
    #Домашняя страница
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Страница для добавления новой темы
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #Страница для добавления новой записи
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #Страница для редактирования записи
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    #Страница чтения записи
    url(r'^read_entry/(?P<entry_id>\d+)/$', views.read_entry, name='read_entry'),
    #Страница поиска
    url(r'^results/(?P<topic_id>\d+)/$', views.entry_search, name='search_entry')
]
