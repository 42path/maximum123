from django.contrib import admin
from .models import Advertisement
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'create_at', 'auction']
    list_filter = ['auction', 'create_at']
    actions = ['make_auction_as_false']

@admin.action(description='Delete auction')
def make_auction_as_false(self, request, queryset):
    queryset.update(auction=False)


admin.site.register(Advertisement, AdvertisementAdmin)