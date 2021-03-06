"""PharmaLiv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path,include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
if django.get_version() >= '2.0.0':
    from django.urls import re_path as url
else:
    from django.conf.urls import url
from patient import views
from pharmacie import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patient.urls')),
    path('', include('connexion.urls')),
    path('', include('sample.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

