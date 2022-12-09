from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from User.models import UserModel
UserModel = get_user_model()

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":'form-control', "placeholder":"Confirm Password"}))
    class Meta:
        model = UserModel
        fields = ('first_name','last_name','email','username','password','confirm_password','image')
        widgets = {
            "first_name" :forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'

            }),
            "last_name" :forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'

            }),
            "email" :forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'

            }),
            "username" :forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'

            }),
            "password" :forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'

            }),
            "confirm_password" :forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password'

            })
        }

    def clean(self):
        super().clean()
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError("Passwords are not equal")


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))