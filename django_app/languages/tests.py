from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Phrase


class LanguagesPageViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.phrase1 = Phrase.objects.create(user=self.user, source_text='Test Source 1', target_text='Test Target 1')
        self.phrase2 = Phrase.objects.create(user=self.user, source_text='Test Source 2', target_text='Test Target 2')
        self.client = Client()

    def test_get_languages_page_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('languages'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['phrases'], map(repr, [self.phrase1, self.phrase2]), ordered=False)

    def test_get_languages_page_not_authenticated(self):
        response = self.client.get(reverse('languages'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('sign_in'))

    def test_post_create_phrase(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('languages'), {'Create': '', 'source_text': 'New Source', 'target_text': 'New Target'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Phrase.objects.filter(user=self.user, source_text='New Source', target_text='New Target').count(), 1)

    def test_post_delete_phrase(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('languages'), {'Delete': '', 'phrase_id': self.phrase1.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Phrase.objects.filter(id=self.phrase1.id).exists())

    def test_post_search_phrases(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('languages'), {'Search': 'Test Target'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['phrases'], map(repr, [self.phrase1, self.phrase2]), ordered=False)
