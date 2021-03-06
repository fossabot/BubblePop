"""bubblepopApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from apiapp import views as view


urlpatterns = [
    url(r'^test', view.test),
    url(r'^check', view.check_url),
    url(r'^articles', view.find_articles),
    url(r'^blacklist', view.blacklist),
    url(r'^change', view.change_blacklist),
    url(r'^report', view.report),
    url(r'^force_crawl', view.force_crawl),
    url(r'^update_media', view.update_media),
]
