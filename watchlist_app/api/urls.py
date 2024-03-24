from django.urls import path
from watchlist_app.api.views import WatchDetailAV,WatchListAV,  StreamPlatformAv

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/', StreamPlatformAv.as_view(), name='stream_platform'),
]
