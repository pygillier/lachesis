# Management urls
from django.urls import path

from ..views import manage

app_name = "manage"

urlpatterns = [path("", manage.IndexView.as_view(), name="index")]
