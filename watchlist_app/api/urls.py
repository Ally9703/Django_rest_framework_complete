from django.urls import path
from watchlist_app.api.views import ReviewList,ReviewDetail, WatchListAV,  StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    
    path('list/', WatchListAV.as_view(), name='movie_list'),
    # path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_platform'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    #path('stream/<int:pk>/review', StreamPlatformAV.as_view(), name='stream_platform'),
    #path('stream/review/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    
]
