from django.contrib import admin

from common.models import ItemData
from common.signals import add_signals


# Register your models here.
class ItemDataAdmin(admin.ModelAdmin):
    list_display = ('title', "author", 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
    list_filter = ('collection', 'status', 'author')
    ordering = ('-created_at', '-updated_at', 'id')


admin.site.register(ItemData, ItemDataAdmin)

add_signals()
