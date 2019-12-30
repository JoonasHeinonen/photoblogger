from django import forms

class PostForm(forms.Form):
    tagline = forms.CharField(label='Headline', max_length=100)
    content = forms.CharField(label='Content', max_length=4000)