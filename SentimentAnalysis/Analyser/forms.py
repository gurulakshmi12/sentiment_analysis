from django import forms

class TextInputForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea, label='Enter text')

class SentimentForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea, label='Enter text')


