from django.contrib import admin
from .models import WaterAnalysis


@admin.register(WaterAnalysis)
class WaterAnalysisAdmin(admin.ModelAdmin):
    list_display = ("id", "ca", "mg", "na", "so4", "others", "created_at")
    readonly_fields = ("created_at",)
    list_filter = ("created_at",)
    search_fields = ("id",)
