from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import RedirectView as RView
from django.views.generic import TemplateView

from ..models import Redirection


# Application index
class IndexView(TemplateView):
    template_name = "redirections/index.html"


# Primary redirection view
class RedirectView(RView):
    def get(self, request, slug):
        redirection = get_object_or_404(
            Redirection,
            slug=slug,
            status=Redirection.RedirectionStatus.PUBLISHED,  # noqa
        )

        if redirection.staged_redirect:
            # Staged redirection, render the page and let
            # the user click on link afterward;
            return render(
                request=request,
                template_name="redirections/staged.html",
                context={"redirection": redirection},
            )

        else:
            # Direct redirection
            permanent = (
                True
                if redirection.redirection_type
                == Redirection.RedirectionType.PERMANENT  # noqa
                else False
            )
            return redirect(redirection.target_url, permanent=permanent)
