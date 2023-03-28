from django.urls import path

from .v1 import PhraseListCreate, PhraseRetrieveUpdateDestroy, RandomPhraseViewSet

urlpatterns = [
    path("phrases", PhraseListCreate.as_view()),
    path("phrases/<int:pk>", PhraseRetrieveUpdateDestroy.as_view()),
    path("phrases/random_phrase", RandomPhraseViewSet.as_view()),
]
