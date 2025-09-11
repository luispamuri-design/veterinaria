
from django.contrib import admin
from django.urls import path
from proyecto import views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vista_login),


    path('loguearser', views.custom_login, name='custom_login'),

    path('logout/', views.custom_logout, name='logout'),


    path('home', views.home, name='home'),
    path('vista_usuario', views.vista_usuario, name='vista_usuario'),


    path('admin/', admin.site.urls)


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)