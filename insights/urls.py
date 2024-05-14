from django.urls import path
from .views import (
    InsightList,
    InsightCreate,
    InsightUpdate,
    InsightDetail,
    InsightDelete,
)

urlpatterns = [
    path("dashboard/", InsightList.as_view(), name="insight-list"),
    path("dashboard/create/", InsightCreate.as_view(), name="insight-create"),
    path("dashboard/<int:pk>/", InsightDetail.as_view(), name="insight-detail"),
    path("dashboard/<int:pk>/update/", InsightUpdate.as_view(), name="insight-update"),
    path("dashboard/<int:pk>/delete/", InsightDelete.as_view(), name="insight-delete"),
]
