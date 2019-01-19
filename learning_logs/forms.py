from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'text', 'micro', 'resist', 'dev', 'ref', 'body']
        labels = {'text': 'Описание партии'}
        widgets = {'text': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
                   'micro': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
                   'resist': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
                   'dev': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
                   'ref': forms.Textarea(attrs={'cols': 40, 'rows': 2})}