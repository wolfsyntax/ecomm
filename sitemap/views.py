#
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# User add-ons here
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.views import View

# Create your views here.
from django.contrib.auth.models import User

@login_required(login_url="auth/login")
def index(request):
    return HttpResponse("HOMEPAGE AUTHENTICATED")

class HomeView(TemplateView):

    template_name = "sitemap/index.html"

    def get_context_data(self, **kwargs):
        context = {"data": User.objects.make_random_password(8,"abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789!@#$%^&*()_-+[]:;\/<>?.,")}
        return context

class AboutView(TemplateView):

    template_name = "sitemap/about.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context

class ShopView(TemplateView):

    template_name = "sitemap/shop.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context