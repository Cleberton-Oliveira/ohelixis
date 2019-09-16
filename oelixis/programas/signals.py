from cuser.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Produto


@receiver(post_save, sender= Produto)
def set_new_user_group(sender, instance, **kwargs):
    responsaveis = instance.responsaveis.all()
    membros = instance.membros.all()
    responsaveis_group = Group.objects.get_or_create(name='responsaveis')[0]
    membros_group = Group.objects.get_or_create(name='membros')[0]

    for user in responsaveis:
        responsaveis_group.user_set.add(user)

    for user in membros:
        membros_group.user_set.add(user)
