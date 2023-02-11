from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from accounts.models import Profile
from django import forms
import re


class MyUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}


class UserChangeForm(forms.ModelForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'about_user', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone = re.sub('[^0-9]', '', phone)
        if phone.startswith('0'):
            phone = f'996{phone[1:]}'
        if not phone.startswith('996'):
            phone = f'996{phone}'
        phone = f'+{phone}'
        return phone

