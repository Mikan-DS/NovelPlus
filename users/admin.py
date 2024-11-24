from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

from users.admin_forms import UserCreationForm, UserChangeForm
from users.models import User, UserContextButton


class UserContextButtonsInline(admin.TabularInline):
    model = UserContextButton
    verbose_name = 'Контекстная кнопка пользователя'
    verbose_name_plural = 'Контекстные кнопки пользователя'
    extra = 1


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", "is_staff", "get_link",)
    list_filter = ("is_staff",)
    fieldsets = (
        (None, {"fields": ("username", "first_name", "last_name", "email", "avatar", "password", "description", "get_link")}),
        ("Разрешения", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff"
            )}
         ),
    )
    inlines = [UserContextButtonsInline]
    search_fields = ("email", "username", "email")
    ordering = ("id",)

    readonly_fields = ('get_link',)

    def get_link(self, obj: User):
        url = reverse('user', args=(obj.id,))
        return format_html(f'<a href="{url}">Открыть</a>')

    get_link.short_description = "Ссылка на сайте"


admin.site.register(User, CustomUserAdmin)
