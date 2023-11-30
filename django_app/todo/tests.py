from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo


class TodoPageViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_get_todo_page_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTrue('update_form' in response.context)
        self.assertTrue('todos' in response.context)
        self.assertQuerysetEqual(response.context['todos'], Todo.objects.filter(user=self.user).order_by('created_at'), ordered=False)

    def test_get_todo_page_not_authenticated(self):
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('sign_in'))

    def test_post_create_todo_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todos'), {'Create': '', 'title': 'New Todo', 'description': 'New Todo Description'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.filter(user=self.user, title='New Todo', description='New Todo Description').count(), 1)

    def test_post_delete_todo_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        todo = Todo.objects.create(user=self.user, title='Test Todo', description='Test Todo Description')
        response = self.client.post(reverse('todos'), {'Delete': '', 'todo_id': todo.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=todo.id).exists())

    def test_post_update_todo_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        todo = Todo.objects.create(user=self.user, title='Test Todo', description='Test Todo Description')
        response = self.client.post(reverse('todos'), {'Update': '', 'todo_id': todo.id, 'title': 'Updated Todo', 'description': 'Updated Todo Description'})
        self.assertEqual(response.status_code, 302)
        updated_todo = Todo.objects.get(id=todo.id)
        self.assertEqual(updated_todo.title, 'Updated Todo')
        self.assertEqual(updated_todo.description, 'Updated Todo Description')
