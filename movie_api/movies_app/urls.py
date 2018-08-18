from django.urls import path, re_path
from .views import MoviesList, MovieDetails, RequestApi
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', MoviesList.as_view()),
    re_path(r'^movies/(?P<pk>[A-Za-z0-9]+)/$', MovieDetails.as_view()),
    path('request_api', RequestApi.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
