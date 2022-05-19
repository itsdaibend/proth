from django import forms

from .models import Todo


class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'completed_at', 'expired_at', 'is_completed', 'label', 'priority', 'status']