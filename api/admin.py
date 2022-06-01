from django.contrib import admin

from api.models import Post


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "created_at", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title", "body")
    list_filter = ("created_at", "updated_at")


admin.site.register(Post, BaseAdmin)
