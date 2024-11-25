from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from common.models import ItemData, ContextButtonType, ItemDataContextButton
from common.signals import add_signals


class ItemDataButtonsInline(admin.TabularInline):
    model = ItemDataContextButton
    verbose_name = 'Контекстная кнопка информационного объекта'
    verbose_name_plural = 'Контекстные кнопки информационных объектов'
    extra = 1


class ItemDataAdmin(admin.ModelAdmin):
    list_display = ('title', "author", 'status', 'created_at', 'updated_at', 'get_link')
    search_fields = ('title', 'author__username')
    list_filter = ('collection', 'status')
    ordering = ('-created_at', '-updated_at', 'id')

    readonly_fields = ('get_link',)

    inlines = [ItemDataButtonsInline]

    def get_link(self, obj: ItemData):
        if obj.collection:  # Проверяем, есть ли коллекция
            url = reverse('item-view', args=(obj.collection.name, obj.id,))
            return format_html(f'<a href="{url}">Открыть</a>')
        else:
            return "-"

    get_link.short_description = "Ссылка на сайте"


admin.site.register(ItemData, ItemDataAdmin)


class ContextButtonTypeAdmin(admin.ModelAdmin):
    list_display = ('verbose', 'name', 'host_regex')
    search_fields = ('verbose', 'name')
    ordering = ('verbose',)


admin.site.register(ContextButtonType, ContextButtonTypeAdmin)

add_signals()
