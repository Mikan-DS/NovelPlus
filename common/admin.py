from django.contrib import admin

from common.models import ItemData, ContextButtonType, ItemDataContextButton
from common.signals import add_signals


class ItemDataButtonsInline(admin.TabularInline):
    model = ItemDataContextButton
    verbose_name = 'Контекстная кнопка информационного объекта'
    verbose_name_plural = 'Контекстные кнопки информационных объектов'
    extra = 1


class ItemDataAdmin(admin.ModelAdmin):
    list_display = ('title', "author", 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
    list_filter = ('collection', 'status')
    ordering = ('-created_at', '-updated_at', 'id')

    inlines = [ItemDataButtonsInline]


admin.site.register(ItemData, ItemDataAdmin)


class ContextButtonTypeAdmin(admin.ModelAdmin):
    list_display = ('verbose', 'name')
    search_fields = ('verbose', 'name')
    ordering = ('verbose',)


admin.site.register(ContextButtonType, ContextButtonTypeAdmin)

add_signals()
