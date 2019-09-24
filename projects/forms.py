from django import forms
from .models import Task
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        labels = {'text': ''}