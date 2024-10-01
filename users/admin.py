from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
    list_display = ("username", "email", "is_staff",)
    list_filter = ("username", "email", "is_staff",)
    fieldsets = (
        (None, {"fields": ("username", "first_name", "last_name", "email", "avatar", "password", "description")}),
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


admin.site.register(User, CustomUserAdmin)
