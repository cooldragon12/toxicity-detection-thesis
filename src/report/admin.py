from django.contrib import admin

from .models import Entry, PlayerDemography


# Register your models here.
class EntryInline(admin.TabularInline):
    model = Entry
    fields = ["text", "screenshot", "description", "emotion", "toxicity", "sentiment"]
    readonly_fields = ["text", "screenshot"]


@admin.register(PlayerDemography)
class PlayerDemographyAdmin(admin.ModelAdmin):
    model = PlayerDemography
    list_display = ["id", "username"]
    inlines = [EntryInline]


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ["id", "date_created", "player_id", "is_text", "is_screenshot", "emotion", "toxicity", "sentiment"]

    def is_screenshot(self, obj):
        if obj.screenshot is not None:
            return "✅"
        return "❌"

    def is_text(self, obj):
        if obj.text is not None:
            return "✅"
        return "❌"
