from django.contrib import admin
from .models import  Channels, Category, Language, Contact
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'createdat', 'updatedat']
    list_filter = ['createdat']

admin.site.register(Category, CategoryAdmin)

class LanguageAdmin(admin.ModelAdmin):

    list_display = ['name', 'createdat', 'updatedat']


admin.site.register(Language, LanguageAdmin)


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'channel_number', 'informations']
    search_fields = ['name']

    def informations(self, object)  ->str:

        return object.description[:20]+"..."
    
admin.site.register(Channels, ChannelAdmin)

class ContactAdmin(admin.ModelAdmin):

    list_display = ['tvwebsite', 'phone_number', 'tv_email']

admin.site.register(Contact, ContactAdmin)
