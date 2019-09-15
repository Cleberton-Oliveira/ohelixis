from django.db import models

class Tipo(models.Model):
    class Meta:
        abstract = True

    tipos = (('0', 'Eletronico'), ('1', 'Eletrodomestico'), ('3', 'Imovel'), ('4', 'Veiculos'), ('5', 'Roupas'), ('6','Esportes'))
    tipos_img = dict([('0', 'eletronico.png'), ('1', 'eletrodomestico.png'), ('3', 'imovel.png'), ('4', 'veiculos.png'), ('5', 'roupas.png'), ('6','esportes.png')])


class Produto(models.Model):

    class Meta:
        verbose_name='Produto'

    nome = models.CharField('Nome do Produto', max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=000.00)
    tipo_produto = models.CharField(max_length=10, choices=Tipo.tipos,)
    # responsavel = models.ForeignKey(null=False, on_delete=models.CASCADE)
    descricao = models.TextField("descrição", blank=True, null=True)
    imagem = models.ImageField('Imagem', blank =True)
    link = models.CharField('Link', max_length=20)

    def __str__(self):
        return self.nome


class Vendas(models.Model):

    class Meta:
        verbose_name='Transação'

    # comprador = models.ForeignKey()
    # vendedor = models.ForeignKey()
    # produto = models

    def __str__(self):
        return self.nome

