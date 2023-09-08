from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView as RView
from .models import Redirection


# Create your views here.
class RedirectView(RView):
    def get(self, request, key):
        redirect = get_object_or_404(Redirection, key=key, status="published")

        if redirect.redirection_code == "301":
            return HttpResponsePermanentRedirect(redirect.target_url)
        else:
            return HttpResponseRedirect(redirect.target_url)
