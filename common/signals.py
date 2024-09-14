from django.db.models.signals import post_migrate, post_delete
from django.dispatch import receiver

from common.models import ItemDataCollection, ItemDataStatus


@receiver(post_migrate)
def create_collection_types(sender, **kwargs):
    default_collection_types = (
        ("game", "Игра"),
        ("sprite", "Спрайт")
    )

    for collection_name, collection_verbose in default_collection_types:
        ItemDataCollection.objects.get_or_create(name=collection_name, verbose=collection_verbose)


@receiver(post_migrate)
def create_status_types(sender, **kwargs):
    default_status_types = (
        ("announce", "Анонс"),
        ("developing", "Разрабатывается"),
        ("completed", "Вышло")
    )

    for collection_name, collection_verbose in default_status_types:
        ItemDataStatus.objects.get_or_create(name=collection_name, verbose=collection_verbose)


def add_signals():
    print("[+] Store signals added")
