from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from arogya import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("accounts/",include("accounts.urls")),
]
