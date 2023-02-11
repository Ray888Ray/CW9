"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    announcements. Add an import:  from my_app import views
    comments. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    announcements. Add an import:  from other_app.views import Home
    comments. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    announcements. Import the include() function: from django.urls import include, path
    comments. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)