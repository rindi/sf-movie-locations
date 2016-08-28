from django import forms

class MovieForm(forms.Form):
    movie_name = forms.CharField(label='Movie name', max_length=100)
