from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path('movie/<int:movie_id>/', views.movie_details, name='movie_details'),
    # cache the page
    # path('movie_redis/<int:movie_id>/', cache_page(60 * 15)(views.movie_details_redis), name='movie_details_redis'),
    path('movie_redis/<int:movie_id>/', views.movie_details, name='movie_details'),

]