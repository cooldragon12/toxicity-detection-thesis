from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.ReportStatsCreateView.as_view(
            {
                "get": "get_stats",
                "post": "create",
            }
        ),
        name="report",
    ),
    path("entry/", views.EntryCreateView.as_view(), name="add-entry"),
]
