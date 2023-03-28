from django import forms

from .models import Phrase


class PhraseCreationForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = [
            "source_lang",
            "target_lang",
            "source_text",
            "target_text",
            "comment",
            "label",
        ]
