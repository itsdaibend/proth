from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import RegularUser


class RegularUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegularUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password confirmation"}
        )

    username = forms.CharField()
    username.widget.attrs.update({"class": "form-control", "placeholder": "Username"})

    email = forms.EmailField()
    email.widget.attrs.update({"class": "form-control", "placeholder": "Email"})

    class Meta(UserCreationForm):
        model = RegularUser
        fields = ("username", "email", "password1", "password2")
