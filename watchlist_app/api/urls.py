from django.urls import path
from watchlist_app.api.views import WatchListAV,    StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    #path('<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_platform'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_detail'),
]
