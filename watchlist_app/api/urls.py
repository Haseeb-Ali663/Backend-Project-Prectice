from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import ReviewList, WatchListAV, WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewDetail, ReviewCreate,StreamPlatformVS
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='movie-details'),
    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/',ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(), name='review-list'),

    path('<int:pk>/reviews/', ReviewList.as_view(), name='review'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    ]
 