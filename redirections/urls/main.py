from django.urls import path

from ..views import main

app_name = "redirections"

urlpatterns = [
    path("", main.IndexView.as_view(), name="index"),
    path("r/<str:slug>", main.RedirectView.as_view(), name="redirect"),
]
