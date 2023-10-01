from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView as RView
from django.views.generic import TemplateView

from ..models import Redirection


# Application index
class IndexView(TemplateView):
    template_name = "redirections/index.html"


# Primary redirection view
class RedirectView(RView):
    def get(self, request, slug):
        redirect = get_object_or_404(
            Redirection,
            slug=slug,
            status=Redirection.RedirectionStatus.PUBLISHED,  # noqa
        )

        if redirect.redirection_type == Redirection.RedirectionType.PERMANENT:
            return HttpResponsePermanentRedirect(redirect.target_url)
        else:
            return HttpResponseRedirect(redirect.target_url)
