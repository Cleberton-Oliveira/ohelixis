from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Produto


# @receiver(post_save, sender=Produto)
# def set_new_user_group(sender, instance, **kwargs):
#     responsavel = instance.responsaveis.all()
#     responsaveis_group = Group.objects.get_or_create(name='responsavel')[0]
#     for user in responsavel:
#         responsaveis_group.user_set.add(user)

