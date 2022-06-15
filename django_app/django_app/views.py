from django.shortcuts import redirect, render
from django.views import View

from todo.models import Todo


class HomePageView(View):
    model = Todo
    template_name = 'home_page.html'
    context = {'page_title': 'Home'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('sign_in')

        self.context['todos'] = Todo.objects.filter(user=request.user, status=2)
        return render(request, 'home_page.html', self.context)