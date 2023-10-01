from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Redirection(TimeStampedModel):
    class RedirectionType(models.IntegerChoices):
        PERMANENT = 301, _("Permanent")
        TEMPORARY = 302, _("Temporary")

    class RedirectionStatus(models.TextChoices):
        DRAFT = "dr", _("Draft")
        PUBLISHED = "pu", _("Published")

    STATUS = Choices("draft", "published")

    slug = models.SlugField(max_length=10, unique=True)
    target_url = models.URLField()
    redirection_type = models.IntegerField(
        choices=RedirectionType.choices, default=RedirectionType.TEMPORARY
    )

    staged_redirect = models.BooleanField(
        default=False, blank=False, null=False
    )  # noqa

    status = models.CharField(
        max_length=2,
        choices=RedirectionStatus.choices,
        default=RedirectionStatus.DRAFT,  # noqa
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("redirections:redirect", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_random_string(8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def human_http_code(self):
        if self.redirection_type == 301:
            return "Permanent (301)"
        else:
            return "Temporary (302)"
