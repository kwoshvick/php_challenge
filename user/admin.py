from django.contrib import admin
from user.models import User, UserCsvFile


@admin.register(UserCsvFile)
class UserCsvFileAdmin(admin.ModelAdmin):
    list_display = ("id", "state", "name", "original_name")
    search_fields = (
        "state",
        "original_name",
    )
    list_per_page = 20


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "national_id", "country")
    search_fields = (
        "first_name",
        "last_name",
    )
    list_per_page = 20
