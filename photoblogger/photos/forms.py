from django import forms

class PostForm(forms.Form):
    tagline = forms.CharField()
    content = forms.CharField()