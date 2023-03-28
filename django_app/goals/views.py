from django.shortcuts import redirect, render
from django.views import View


class GoalsPageView(View):
    context = {"page_title": "Goals"}

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("sign_in")

        self.context["goals"] = Goal.objects.filter(user=request.user)
        return render(request, "goals/goals_page.html", self.context)
