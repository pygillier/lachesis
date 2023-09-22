# Management urls
from django.urls import path

from ..views import manage

app_name = "manage"

urlpatterns = [
    path("", manage.IndexView.as_view(), name="index"),
    path("redirections/", manage.RedirectionListView.as_view(), name="redirections"),
    path("redirections/new", manage.RedirectionCreateView.as_view(), name="new"),
    path("redirections/update/<str:key>", manage.RedirectionUpdateView.as_view(), name="update"),
]
