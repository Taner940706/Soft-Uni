from django.shortcuts import render
from django.views import generic as views

from unit_and_integration_testing.web.models import Profile


class ProfilesListView(views.ListView):
    template_name = 'profile/list.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profiles_count'] = self.object_list.count()

        return context
