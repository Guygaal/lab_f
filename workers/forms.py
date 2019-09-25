from django import forms
from .models import Emp
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from projects.models import Task

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['text']
        labels = {'text': ''}


class AddTasks(forms.Form):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.order_by('text'),
        widget=forms.CheckboxSelectMultiple,
    )

'''class AddTasks(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        labels = {'text': 'Проект:'}
        widgets = {'text': forms.CheckboxSelectMultiple
                   }'''
