from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import ReviewList, WatchListAV, WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/',ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(), name='review-list'),

    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    ]
 