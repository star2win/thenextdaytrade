"""
URL configuration for thenextdaytrade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path('login/', hello.views.login_view, name='login'),
    path('logout/', hello.views.logout_view, name='logout'),
    path('trader/', hello.views.trader_view, name='trader'),
    path('reader/', hello.views.reader_view, name='reader'),
    path('api/validate-ticker/', hello.views.validate_ticker, name='validate_ticker'),
    # Uncomment this and the entry in `INSTALLED_APPS` if you wish to use the Django admin feature:
    # https://docs.djangoproject.com/en/5.1/ref/contrib/admin/
    path("admin/", admin.site.urls),
]
