# artist_api/views.py

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as django_filters
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class WorkFilter(django_filters.FilterSet):
    work_type = django_filters.ChoiceFilter(choices=Work.WORK_TYPES)

    class Meta:
        model = Work
        fields = ['work_type']

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = WorkFilter

class ArtistWorkListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]

class ArtistSearchView(generics.ListAPIView):
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.kwargs['name']
        return Artist.objects.filter(name__icontains=name)

