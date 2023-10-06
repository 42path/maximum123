from django.contrib import admin
from .models import Advertisement
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'create_date', 'auction', 'image']
    list_filter = ['auction', 'create_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('General', {'fields': ('title', 'description', 'image'),}),
        ('Finance', {'fields': ('price', 'auction'),
        'classes': ['collapse']})

    )

    @admin.action(description='Delete auction')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='Add auction')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)