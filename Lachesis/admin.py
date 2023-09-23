from django.contrib import admin
from django.urls import reverse_lazy


class LachesisAdminSite(admin.AdminSite):
    site_header = "Lachesis"
    site_title = "Lachesis admin site"
    site_url = reverse_lazy("manage:index")
