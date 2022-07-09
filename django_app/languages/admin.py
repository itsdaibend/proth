from django.contrib import admin

from .models import LanguagesLabel, Phrase

admin.site.register(Phrase)
admin.site.register(LanguagesLabel)
