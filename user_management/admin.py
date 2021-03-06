from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user_management.forms import UserChangeForm, UserCreationForm
from user_management.models import UserProfile


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "gender",
                    "food_preference",
                    "first_name",
                    "last_name",
                    "birth_date",
                    "phone",
                    "address_line_1",
                    "zip",
                    "city",
                    "state",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "user_permissions")}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password",
                    "password_validation",
                    "gender",
                    "food_preference",
                    "first_name",
                    "last_name",
                    "birth_date",
                    "phone",
                    "address_line_1",
                    "zip",
                    "city",
                    "state",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(UserProfile, UserAdmin)
