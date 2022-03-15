"""imagesproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from docs.views import home_view, file_upload, arr_view,login_user,logout_user,register_user,welcome_view,collection_view,ablumshare_view


urlpatterns = [
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path('register', register_user, name="register_user"),
    path('admin/', admin.site.urls),
    path('home', home_view),
    path('', welcome_view),
    path('upload/', file_upload),
    path('show/', arr_view),
    path('collection', collection_view),
    path('album/<str:str>', ablumshare_view),
    path('members', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
