from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchListApp.api.views import (ReviewCreate, ReviewList, ReviewDetail, 
                                    WatchListAV, WatchDetailAV, 
                                    StreamPlatformMVS, StreamPlatformAV, 
                                    StreamPlatformDetailAV)

router = DefaultRouter()
router.register('stream', StreamPlatformMVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]