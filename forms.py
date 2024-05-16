from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """A class to represent a form for users adding new topics."""
    class Meta:
        model = Topic  # tells Django to build a form from the Topic model.
        fields = ['text']  # build a form that includes just the text field.
        labels = {'text': ''}  # does not generate a label for the text field.


class EntryForm(forms.ModelForm):
    """A class to represent a form for users adding new entries for a topic."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # overrides default widget for more writing space

