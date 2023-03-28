from django.urls import path

from .views import SignInPageView, SignOutPageView, SignUpPageView

urlpatterns = [
    path("sign_in/", SignInPageView.as_view(), name="sign_in"),
    path("sign_up/", SignUpPageView.as_view(), name="sign_up"),
    path("sign_out/", SignOutPageView.as_view(), name="sign_out"),
]
