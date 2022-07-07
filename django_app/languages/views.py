from django.shortcuts import redirect, render
from django.views import View


class LanguagesPageView(View):
    context = {'page_title': 'Languages'}

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('sign_in')

        return render(request, 'languages/languages_page.html', self.context)
