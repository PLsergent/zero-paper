from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('user/', include('django.contrib.auth.urls')),
    path('login/',views.login,name='login')
]