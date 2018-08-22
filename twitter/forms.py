from django import forms
from django.contrib.auth.models import User
from .models import Tweet

class TweetForm(forms.ModelForm):
    body = forms.CharField(
            max_length = 140,
            label = '',
            widget = forms.Textarea(attrs={'placeholder': "What's happening?", 'rows': 5, 'cols': 70})
            )
    class Meta:
        model = Tweet
        fields = ('body',)
