from django import forms


class SubmitMovieForm(forms.Form):
    title = forms.CharField()
