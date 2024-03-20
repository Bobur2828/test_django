from django.contrib import admin
from .models import Place,PlaceComment,PlaceOwner,Owner

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address')
    search_fields = ('id', 'name')

admin.site.register(Place, PlaceAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio')
    search_fields = ('id', 'name')

admin.site.register(Owner, OwnerAdmin)

admin.site.register(PlaceComment)
admin.site.register(PlaceOwner)
