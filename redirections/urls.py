from django.urls import path
from . import views

urlpatterns = [
    path("r/<str:key>", views.RedirectView.as_view(), name="redirect"),
]
