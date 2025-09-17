
from django.contrib import admin
from django.urls import path, include
from proyecto import views as views
from django.conf import settings
from django.conf.urls.static import static
#from  .views import test_db  # Ajusta según tu app




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proyecto.urls')),
    
    path('', views.vista_login),



    path('loguearser', views.custom_login, name='custom_login'),

    path('logout/', views.custom_logout, name='logout'),


    path('home', views.home, name='home'),
    path('vista_usuario', views.vista_usuario, name='vista_usuario'),

    #path('test_db/', test_db, name='test_db'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)