
from django.contrib import admin
from django.urls import path
from proyecto import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vista_login),


    path('loguearser', views.custom_login, name='custom_login'),

    path('home', views.home, name='home'),
]
