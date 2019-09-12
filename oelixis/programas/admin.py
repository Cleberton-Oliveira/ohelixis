from django.contrib import admin
from .models import Produto, Vendidos, Comprados

admin.site.register(Produto)
admin.site.register(Vendidos)
admin.site.register(Comprados)
