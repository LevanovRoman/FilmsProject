from django.urls import path
from .views import *

urlpatterns = [
    path('', MoviesView.as_view()),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name='actor_detail'),
    # path('', GenreAll.as_view(), name='genre'),
    # path('<slug:slug>/', GenreView.as_view(), name='genre_detail'),
]