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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, handler400, handler403, handler404, handler500
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^", include(("core.urls", "core")), name="core"),
    url(r"^", include(("sitemap.urls", "sitemap")), name="sitemap"),
    url(r"^auth/", include(("authentication.urls", "authentication")), name="authentication"),
    url(r'^test/$', TemplateView.as_view(template_name="errors/e404.html"), name="test-unit"),
]

handler400 = "errors.views.e400"    #bad request
handler403 = "errors.views.e403"    #permission denied
handler404 = "errors.views.e404"    #page not found
handler500 = "errors.views.e500"    #server error
