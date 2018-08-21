from django import forms
from django.contrib.auth.models import User
from .models import Tweet

class SignupForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        email = cleaned_data.get('email')
        if User.objects.get(email=email):
            raise forms.ValidationError('That email is already in use.')

class TweetForm(forms.ModelForm):
    body = forms.CharField(
            max_length = 140,
            label = '',
            widget = forms.Textarea(attrs={'placeholder': "What's happening?", 'rows': 5, 'cols': 70})
            )
    class Meta:
        model = Tweet
        fields = ('body',)
