from django.db import models
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices
from django.conf import settings
from django.utils.crypto import get_random_string


class Redirection(TimeStampedModel):
    STATUS = Choices("draft", "published")
    REDIRECTION_CODE = Choices("301", "302")

    key = models.CharField(max_length=10, unique=True)
    target_url = models.URLField()
    redirection_code = StatusField(choices_name="REDIRECTION_CODE")
    status = StatusField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = get_random_string(8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key

    def human_http_code(self):
        if self.redirection_code == "301":
            return "Permanent (301)"
        else:
            return "Temporary (302)"
