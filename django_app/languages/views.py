from django.shortcuts import redirect, render
from django.views import View

from .models import Phrase


class LanguagesPageView(View):
    context = {'page_title': 'Languages'}

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('sign_in')

        self.context['phrases'] = Phrase.objects.filter(user=request.user)
        return render(request, 'languages/languages_page.html', self.context)
