from django.shortcuts import redirect, render
from django.views import View

from .models import Phrase
from .forms import PhraseCreationForm


class LanguagesPageView(View):
    context = {'page_title': 'Languages'}

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('sign_in')
        
        form = PhraseCreationForm()

        self.context['form'] = form
        self.context['phrases'] = Phrase.objects.filter(user=request.user)
        return render(request, 'languages/languages_page.html', self.context)
    
    def post(self, request, phrase_id=None):
        if 'Create' in request.POST:
            form = PhraseCreationForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.save()

                return redirect('languages')

        elif 'Delete' in request.POST:
            if request.method == "POST":
                phrase = Phrase.objects.get(id=phrase_id)
                phrase.delete()

                return redirect('languages')
