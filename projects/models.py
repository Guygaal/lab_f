from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """Проект"""
    emps = models.ManyToManyField('workers.Emp')
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
 #   owner = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text
