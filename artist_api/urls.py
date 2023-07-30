# artist_api/urls.py

from django.urls import path
from .views import WorkListCreateView, ArtistWorkListCreateView, ArtistSearchView

urlpatterns = [
    path('works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('works/<int:pk>/', WorkDetailUpdateDeleteView.as_view(), name='work-detail-update-delete'),
    path('artists/', ArtistWorkListCreateView.as_view(), name='artist-work-list-create'),
    path('artists/<str:name>/', ArtistSearchView.as_view(), name='artist-search'),
]
