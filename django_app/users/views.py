from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import RegularUserCreationForm


class SignInPageView(View):
    context = {"page_title": "Sign in"}

    def get(self, request, *args, **kwargs):
        return render(request, "users/sign_in.html", self.context)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is invalid")
            return render(request, "users/sign_in.html", self.context)


class SignUpPageView(View):
    context = {"page_title": "Sign up"}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            form = RegularUserCreationForm()
            self.context["form"] = form
            return render(request, "users/sign_up.html", self.context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            form = RegularUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data["username"]
                messages.success(request, f"Account for {user} has created successfuly")
                return redirect("sign_in")

            self.context["form"] = form
            return render(request, "users/sign_up.html", self.context)


class SignOutPageView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("sign_in")
        else:
            logout(request)
            messages.info(request, "You successfuly log out. Now, please authenticate")
            return redirect("sign_in")
