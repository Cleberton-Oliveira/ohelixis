from django.contrib import admin
from django.db.models import Q
from .models import Produto, Vendas
# from .forms import ProdutoForm
from unicodedata import normalize
from django.utils.html import format_html


class ProdutoAdmin(admin.ModelAdmin):
    # form = ProdutoForm
    list_display = ('nome', 'image_tag')
    readonly_fields = ('responsavel', 'vendido', 'link')

    def get_actions(self, request):
        actions = super(ProdutoAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        gLink = obj.nome.lower()
        gLink = gLink.replace(" ", "-")
        gLink = normalize('NFKD', gLink)
        obj.link = gLink
        obj.save()

    def image_tag(self, obj):
        if obj.imagem:
            return format_html('<img src="/media/{}" width="50" height="50"/>'.format(obj.imagem))
            format_html('<img src="{}" width="50" height="50"/>')
        else:
            return format_html('<p>Sem imagem</p>')

    def get_queryset(self, request):
        qs = super(ProdutoAdmin, self).get_queryset(request)
        return qs.filter(responsavel = request.user)



class VendasAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(VendasAdmin, self).get_queryset(request)
        return qs.filter(Q(comprador=request.user) | Q(vendedor=request.user))

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Vendas, VendasAdmin)
