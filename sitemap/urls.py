"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url
from . import views as mview
from sitemap.views import HomeView#, AboutView, ShopView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    #url(r'^x$', mview.index, name="xhome"),
    #url(r'^about$', AboutView.as_view(), name="about"),
    #url(r'^shop$', ShopView.as_view(), name="shop"),

    #url(r'^$', TemplateView.as_view(template_name="sitemap/index.html"), name="home"),
    #url(r'^x$', mview.index, name="xhome"),

    url(r'^about$', TemplateView.as_view(template_name="sitemap/about.html"), name="about"),
    url(r'^shop$', TemplateView.as_view(template_name="sitemap/shop.html"), name="shop"),
    url(r'^faq$', TemplateView.as_view(template_name="sitemap/faq.html"), name="faq"),
    #url(r'^$', mview.index, name="home"),
]
