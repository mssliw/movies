import requests
from django import forms
from django.conf import settings


class SubmitMovieForm(forms.Form):
    """
    Get title of the movie and request external API
    """
    title = forms.CharField()

    def search(self):
        title = self['title'].data
        if title is not None:
            result = {}
            api_key = settings.OMDB_KEY
            url = 'http://www.omdbapi.com/?apikey={}&t={}'.format(api_key, title)
            response = requests.get(url)
            if response.status_code == 200:
                result = response.json()
                result['success'] = True
            else:
                result['success'] = False
                if response.status_code == 404:
                    print('404')
                else:
                    print('error occured')
            return result
