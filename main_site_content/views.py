from django.views.generic import DetailView
from .models import MainSiteContent


class MainSiteView(DetailView):
    model = MainSiteContent
    template_name = 'base.html'

    def get_object(self, queryset=None):
        if not queryset:
            return self.model.objects.get(is_live=True)
        return queryset
