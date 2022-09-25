from django import forms
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.password_validation import validate_password, get_default_password_validators

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput)
    is_staff = forms.BooleanField(required=False, initial=False)

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if validate_password(password1, None, get_default_password_validators()) is not None:
            raise forms.ValidationError("This password is invalid")
        return password1

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This is an username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(username__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid User")
        return username
        