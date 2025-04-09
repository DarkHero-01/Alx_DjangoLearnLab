from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Define group-permission mappings
    group_permissions = {
        'Viewers': ['can_view'],
        'Editors': ['can_view', 'can_create', 'can_edit'],
        'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
    }

    book_ct = ContentType.objects.get_for_model(Book)

    for group_name, perms in group_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for codename in perms:
            permission = Permission.objects.get(codename=codename, content_type=book_ct)
            group.permissions.add(permission)