from django.contrib import admin
from programas import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('registration', views.registration, name='registration'),
    path('logout/', views.sair, name='logout'),
]
