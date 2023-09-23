# managmeent views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from ..models import Redirection


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "manage/index.html"


class RedirectionListView(LoginRequiredMixin, ListView):
    model = Redirection
    template_name = "manage/redirection_list.html"
    context_object_name = "redirections"

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.filter(author=self.request.user)


class RedirectionCreateView(LoginRequiredMixin, CreateView):
    model = Redirection
    template_name = "manage/redirection_form.html"
    success_url = reverse_lazy("manage:redirections")
    fields = ["target_url", "status", "redirection_code"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RedirectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Redirection
    template_name = "manage/redirection_form.html"

    fields = ["target_url", "status", "redirection_code"]

    success_url = reverse_lazy("manage:redirections")
