from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publish', 'price', 'list_date', 'realtor')
    list_display_links = ('title',)
    list_filter = ('realtor', 'title')
    list_editable = ('is_publish',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)

