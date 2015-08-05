"""shineidealab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from main_web.views import page_home, page_about, page_projects, page_release, page_contact

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', page_home, name='page_home'),
    url(r'^home/', page_home, name='page_home'),
    url(r'^about/', page_about, name='page_about'),
    url(r'^projects/', page_projects, name='page_projects'),
    url(r'^release/', page_release, name='page_release'),
    url(r'^contact/', page_contact, name='page_contact'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)