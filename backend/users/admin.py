from django.contrib import admin

from users.models import Follow


@admin.register(Follow)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user', 'author')
    empty_value_display = '-empty-'
