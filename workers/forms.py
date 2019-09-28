from django import forms
from .models import Emp
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from projects.models import Task


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['text']
        labels = {'text': ''}


class AddTasks(forms.ModelForm):
    task = Task.objects.order_by('text')

    class Meta:
        model = Emp
        fields = ['tasks']


'''class AddTasks(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        labels = {'text': 'Проект:'}
        widgets = {'text': forms.CheckboxSelectMultiple
                   }'''
