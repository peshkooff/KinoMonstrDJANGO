from django import forms
from .models import AdvUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ChangeUserInfo(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адресс електронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')