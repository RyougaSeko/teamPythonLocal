from django import forms
from .models import *


class MemoForm(forms.ModelForm):
    problem = forms.CharField(label='課題', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    policy = forms.CharField(label='方針', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    winner = forms.CharField(label='勝敗', widget=forms.TextInput(attrs={'readonly':'readonly', 'style': 'width: 100%;'}))

    class Meta:
        model = Memo
        fields = ['problem', 'policy', 'winner']
