from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from catalog.forms import StyleFormMixin
from users.models import User


class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserAuthenticationForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User

class RestorePasswordForm(StyleFormMixin, forms.Form):
    email = forms.EmailField()