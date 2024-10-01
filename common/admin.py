from django.contrib import admin

from common.models import ItemData, ContextButtonType
from common.signals import add_signals


# Register your models here.
class ItemDataAdmin(admin.ModelAdmin):
    list_display = ('title', "author", 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
    list_filter = ('collection', 'status')
    ordering = ('-created_at', '-updated_at', 'id')


admin.site.register(ItemData, ItemDataAdmin)


class ContextButtonTypeAdmin(admin.ModelAdmin):
    list_display = ('verbose', 'name')
    search_fields = ('verbose', 'name')
    ordering = ('verbose',)


admin.site.register(ContextButtonType, ContextButtonTypeAdmin)

add_signals()
