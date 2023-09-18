# managmeent views
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "manage/index.html"
