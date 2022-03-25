"""vuqar_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from homepage.views import homepage
from service.views import service
from blog.views import blog
from about.views import about
from appoinment.views import appoinment
from contact.views import contact
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('', include('blog.urls', namespace='blogapp')),
    path('', include('service.urls', namespace="serviceapp")),
    path('bloq/', blog, name="bloq"),
    path('about/', about, name="about"),
    path('service/', service, name="service"),
    path('appoinment/', appoinment, name="appoinment"),
    path('contact/', contact, name="contact"),
#     path('sitemap.xml/', sitemap, name='django.contrib.sitemaps.views.sitemap'),
#     path('robots.txt/', robots, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap.xml/', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
]
