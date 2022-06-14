from django.shortcuts import redirect
from django.views.generic import ListView

from todo.models import Todo


class HomePageView(ListView):
    model = Todo
    template_name = 'home_page.html'
    context_object_name = 'todos'
    extra_context = {'page_title': 'Home'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return redirect('sign_in')

        return Todo.objects.filter(user=self.request.user, status=2)