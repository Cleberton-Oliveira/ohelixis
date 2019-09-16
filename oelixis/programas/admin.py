from django.contrib import admin
from django.db.models import Q
from .models import Produto, Vendas
from .forms import ProdutoForm
from unicodedata import normalize
from django.utils.html import format_html



class ProdutoAdmin(admin.ModelAdmin):


    form = ProdutoForm
    list_display = ('nome', 'image_tag')
    # list_filter = ('responsaveis', 'membros',)
    #
    # def get_readonly_fields(self, request, obj=None):
    #     qs = super(ProdutoAdmin, self).get_queryset(request)
    #     qsResp = qs.filter(responsaveis=request.user)
    #     qsMemb = qs.filter(membros=request.user)
    #     if obj in qsResp or request.user.is_superuser:
    #         return []
    #     if obj in qsMemb:
    #         return ('nome', 'responsaveis', 'membros', 'preco', 'tipo_produto', 'descricao','imagem')
    #     return []

    def get_actions(self, request):
        actions = super(ProdutoAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    # def get_queryset(self, request):
    #     qs = super(ProdutoAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(Q(responsaveis=request.user) | Q(membros=request.user)).distinct()


    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


    def save_model(self, request, obj, form, change):
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


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Vendas)
