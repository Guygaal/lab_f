from django import forms
from .models import Topic, Entry
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'microch', 'current', 'voltage', 'wd', 'ss', 'diaf', 'hs', "n", 'micro_adv', 'resist',
                  'resist_rpm', 'resist_time', 'dry_type', 'dry_temp', 'dry_time', 'dev', 'dev_time', 'ref',
                  'ref_temp', 'ref_time', 'tr_rec', 'tr_time', 'tr_vel', 'pyth', 'gds', 'body']
        labels = {'text': 'Описание партии'}
        widgets = {'text': forms.Textarea(attrs={'cols': 200, 'rows': 2}),
                   'micro_adv': forms.Textarea(attrs={'cols': 200, 'rows': 2}),
                   'tr_rec': forms.Textarea(attrs={'cols': 40, 'rows': 1}),
                   'body': SummernoteInplaceWidget()
                   }


class EntryReadForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'microch', 'current', 'voltage', 'wd', 'ss', 'diaf', 'hs', "n", 'micro_adv', 'resist',
                  'resist_rpm', 'resist_time', 'dry_type', 'dry_temp', 'dry_time', 'dev', 'dev_time', 'ref', 'ref_temp',
                  'ref_time', 'tr_rec', 'tr_time', 'tr_vel', 'pyth', 'gds', 'body']
        labels = {'text': 'Описание партии'}
        widgets = {'body': SummernoteInplaceWidget()}
