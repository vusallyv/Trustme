from django.contrib import admin

from core.models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company_name',
                    'phone_prefix', 'phone')
    list_filter = ('full_name', 'email', 'company_name',
                   'phone_prefix', 'phone')
    search_fields = ('full_name', 'email', 'company_name')


admin.site.register(Contact, ContactAdmin)
