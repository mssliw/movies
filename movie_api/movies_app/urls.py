from django.urls import path, re_path
from .views import MoviesListView, MovieDetailsView, CommentView, MovieCommentsView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('movies/', MoviesListView.as_view()),
    re_path(r'^movies/(?P<pk>[A-Za-z0-9]+)/$', MovieDetailsView.as_view()),
    path('comments/', CommentView.as_view()),
    re_path(r'^comments/(?P<pk>[0-9]+)/$', MovieCommentsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
