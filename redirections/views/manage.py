# managmeent views
from django.views.generic import TemplateView, ListView
from ..models import Redirection
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "manage/index.html"


class RedirectionListView(LoginRequiredMixin, ListView):
    model = Redirection
    template_name = "manage/redirection_list.html"
