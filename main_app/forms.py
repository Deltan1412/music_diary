from django import forms
from django.contrib.auth.models import User
from .models import Entry

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'song_owner', 'content']