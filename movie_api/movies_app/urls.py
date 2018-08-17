from django.urls import path, include
from django.conf.urls import url
from . import views
# from .views import RequestView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
# router.register('movies_app', views.MovieView)
# router.register('movies/', RequestView.as_view(), base_name='movie')

urlpatterns = [
    path('movies/', views.movies_list),
    path('movies/<pk>', views.movie_details),
    # path('', include(router.urls)),
    # path('movies/', RequestView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)