from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("predicted_label", "score", "created_at")
    search_fields = ("text",)
