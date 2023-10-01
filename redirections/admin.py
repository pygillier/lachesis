from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Redirection)
class RedirectionAdmin(ModelAdmin):
    list_display = ("slug", "status", "http_code", "target_url", "link_copy")
    list_filter = ("status", "redirection_code")
    exclude = ("slug",)

    actions = ["make_published"]

    @admin.display(description="Copy link")
    def link_copy(self, obj: models.Redirection):
        return format_html(
            '<a href="{}" data-link="{}">Copy link</a>',
            obj.get_absolute_url(),
            obj.target_url,
        )

    @admin.display(description="HTTP redirection")
    def http_code(self, obj: models.Redirection):
        if obj.status == "301":
            return "Permanent (301) "
        else:
            return "Temporary (302)"

    @admin.action(description="Publish selected redirections")
    def make_published(self, request, queryset) -> None:
        queryset.update(status="published")
