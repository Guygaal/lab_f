from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField(blank=True, null=True, verbose_name='Описание партии')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название партии')
    micro = models.TextField(blank=True, null=True, verbose_name='Микроскоп')
    resist = models.TextField(blank=True, null=True, verbose_name='Резист')
    dev = models.TextField(blank=True, null=True, verbose_name='Проявка')
    ref = models.TextField(blank=True, null=True, verbose_name='Reflow')
    body = RichTextUploadingField(blank=True, null=True, verbose_name='Дополнительное поле; изображения, таблицы')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."
# Create your models here.
