from django.contrib import admin
from programas import views
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import reverse
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('registration', views.registration, name='registration'),
    path('logout/', views.sair, name='logout'),
    path('<slug:produto>/', views.produtoSelecionado, name='produtos'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
