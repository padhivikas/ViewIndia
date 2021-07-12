"""viewindia URL Configuration

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
from django.urls import path , include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from rest_framework import routers

router = routers.DefaultRouter() 
router.register(r'blog', views.BlogViewset)
router.register(r'user', views.UserViewset)
router.register(r'contact', views.ContactViewset)



urlpatterns = [
    path('',RedirectView.as_view(url="blog/")),
    path('blog/', include('blog.urls')),
    path('profile/', include('userprofile.urls')),
    path('accounts/', include('registration.backends.simple.urls') , name="account"),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path(r'api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

