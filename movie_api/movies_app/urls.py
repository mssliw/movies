from django.urls import path, re_path
from .views import MoviesListView, MovieDetailsView, CommentView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('movies/', MoviesListView.as_view()),
    path('comments/', CommentView.as_view()),
    re_path(r'^movies/(?P<pk>[A-Za-z0-9]+)/$', MovieDetailsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
