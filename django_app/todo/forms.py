from django import forms

from .models import Todo


class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'expired_at', 'label', 'priority', 'status']
        widgets = {
            'expired_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class TodoUpdateForm(forms.ModelForm):
    todo_id = forms.IntegerField(widget = forms.HiddenInput())
    title = forms.CharField(required=False)
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'expired_at', 'label', 'priority', 'status', "todo_id"]
        widgets = {
            'expired_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }