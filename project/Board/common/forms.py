from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    rank = forms.CharField(label="계급")

    class Meta:
        model = User
        fields = ("username", "rank", "password1", "password2", "email")