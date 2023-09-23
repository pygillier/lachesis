from django.contrib.admin.apps import AdminConfig


class LachesisAdminConfig(AdminConfig):
    default_site = "Lachesis.admin.LachesisAdminSite"
