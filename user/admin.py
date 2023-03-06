from django.contrib import admin

from user.models import UserCsvFile


@admin.register(UserCsvFile)
class LoanRepayment(admin.ModelAdmin):
    list_display = ("id", "state", "name", "original_name")
    list_per_page = 20
