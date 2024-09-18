from django.db.models.signals import post_migrate, post_delete
from django.dispatch import receiver

from common.models import ItemDataCollection, ItemDataStatus


@receiver(post_migrate)
def create_collection_types(sender, **kwargs):
    default_collection_types = (
        ("game", "Игра"),
        ("sprite", "Спрайт"),

        ("developer", "Работник"),
        ("project", "Проект"),
    )

    for collection_name, collection_verbose in default_collection_types:
        try:
            ItemDataCollection.objects.get_or_create(name=collection_name, verbose=collection_verbose)
        except:
            pass


@receiver(post_migrate)
def create_status_types(sender, **kwargs):
    default_status_types = (
        ("announce", "Анонс"),
        ("developing", "Разрабатывается"),
        ("completed", "Вышло"),

        ("active_search", "Активный поиск"),
        ("not_search", "Поиск завершен"),
        ("search", "Принимаются заявки"),
    )

    for collection_name, collection_verbose in default_status_types:
        try:
            ItemDataStatus.objects.get_or_create(name=collection_name, verbose=collection_verbose)
        except:
            pass


def add_signals():
    print("[+] Store signals added")
