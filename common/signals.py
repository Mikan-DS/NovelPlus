from django.db.models.signals import post_migrate, post_delete
from django.dispatch import receiver

from common.models import ItemDataCollection, ItemDataStatus, ContextButtonType


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
        except Exception as e:
            print(f"[-] {repr(e)} - {collection_name} {collection_verbose}")

@receiver(post_migrate)
def create_context_button_types(sender, **kwargs):
    default_context_button_types = (
        ("telegram", "Телеграм"),
        ("vk", "Вконтакте"),
        ("email", "E-MAIL"),
        ("steam", "Страница в стиме"),
        ("itchio", "Страница в itch.io"),
    )

    for name, verbose in default_context_button_types:
        try:
            ContextButtonType.objects.get_or_create(name=name, verbose=verbose)
        except Exception as e:
            print(f"[-] {repr(e)} - {name} {verbose}")




def add_signals():
    print("[+] Common signals added")
