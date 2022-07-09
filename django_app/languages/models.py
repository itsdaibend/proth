from django.conf import settings
from django.db import models


class LanguagesLabel(models.Model):
    label = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Labels"
    
    def __str__(self):
        return f"{self.label}"

class Phrase(models.Model):
    class LanguageToChoose(models.TextChoices):
        ENGLISH = '1', 'English'
        UKRAINIAN = '2', 'Ukrainian'
        RUSSIAN = '3', 'Russian'
        GERMAN = '4', 'German'
        POLISH = '5', 'Polish'
        ITALIAN = '6', 'Italian'
        FRENCH = '7', 'French'
        SPANISH = '8', 'Spanish'
        TURKISH = '9', 'Turkish'

    DEFAULT_LABEL_ID = 1 # 'Other'

    source_lang = models.CharField(max_length=2, choices=LanguageToChoose.choices, default=LanguageToChoose.ENGLISH)
    target_lang = models.CharField(max_length=2, choices=LanguageToChoose.choices, default=LanguageToChoose.RUSSIAN)
    source_text = models.CharField(max_length=200)
    target_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200, blank=True)
    label = models.ForeignKey(LanguagesLabel, default=DEFAULT_LABEL_ID, on_delete=models.CASCADE)
    translated_times = models.PositiveIntegerField(default=0, blank=True)
    not_translated_times = models.PositiveIntegerField(default=0, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.source_text}'
