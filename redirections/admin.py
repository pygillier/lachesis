from django.contrib import admin

from . import models


@admin.register(models.Redirection)
class RedirectionAdmin(admin.ModelAdmin):
    list_display = ("key", "status", "human_http_code", "target_url")
    exclude = ("key",)

    actions = ["make_published"]

    @admin.action(description="Publish selected redirections")
    def make_published(self, request, queryset) -> None:
        queryset.update(status="published")
