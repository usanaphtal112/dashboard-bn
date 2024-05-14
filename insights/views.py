from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from drf_spectacular.utils import extend_schema
from .models import Insight
from .serializers import InsightSerializer


@extend_schema(
    description="Display the Dashboard data",
    tags=["Dashboard"],
)
class InsightList(ListAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer


@extend_schema(
    description="Display the Dashboard data",
    tags=["Dashboard"],
)
class InsightCreate(CreateAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer


@extend_schema(
    description="Display the Dashboard user details",
    tags=["Dashboard"],
)
class InsightDetail(RetrieveAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer
    lookup_field = "pk"


@extend_schema(
    description="Update the Dashboard data",
    tags=["Dashboard"],
)
class InsightUpdate(UpdateAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer
    lookup_field = "pk"


@extend_schema(
    description="Delete the Dashboard data",
    tags=["Dashboard"],
)
class InsightDelete(DestroyAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer
    lookup_field = "pk"
