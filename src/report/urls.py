from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.ReportView.as_view(), name="add-report"),
]
