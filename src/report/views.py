from typing import Any, Type

from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Entry, PlayerDemography
from .serializer import EntrySerializer, ReportSerializer


# # Create your views here.
# class ReportStatsCreateView(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     queryset = PlayerDemography.objects.all()
#     queryset_entry = Entry.objects.all()
#     serializer_class = ReportSerializer

#     def get_stats(self, request, *args, **kwargs):
#         player_count = self.queryset.count()
#         entry_count = self.queryset_entry.count()
#         return Response(data={"players_count": player_count, "entries_count": entry_count}, status=200)


@parser_classes([MultiPartParser])
class EntryCreateView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
