from cuser.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from cuser.models import CUser
from .models import Produto


@receiver(post_save, sender= CUser)
def set_new_user_group(sender, instance, **kwargs):
    user = CUser.objects.get(id=instance.id)
    membros_group = Group.objects.get_or_create(name='Usuarios')[0]
    membros_group.user_set.add(user)


# @receiver(post_save, sender= Produto)
# def exclude_produto(sender, instance, **kwargs):