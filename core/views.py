#
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# User add-ons here
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.views import View

# Create your views here.

#@login_required(login_url="")


class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = '/auth/login/'
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context