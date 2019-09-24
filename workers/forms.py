from django import forms
from .models import Emp
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['text']
        labels = {'text': ''}