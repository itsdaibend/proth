from django.urls import path

from .views import LanguagesPageView


urlpatterns = [
    path('', LanguagesPageView.as_view(), name='languages'),
    path('delete/<int:phrase_id>', LanguagesPageView.as_view(), name='languages')
]