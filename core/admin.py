from django.contrib import admin

from core.models import Applicant, Contact, Vacancy

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company_name',
                    'phone_prefix', 'phone')
    list_filter = ('full_name', 'email', 'company_name',
                   'phone_prefix', 'phone')
    search_fields = ('full_name', 'email', 'company_name')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    list_filter = ('type',)
    search_fields = ('title', 'short_description', 'full_description')
    exclude = ('slug',)


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'vacancy')
    list_filter = ('full_name', 'vacancy')
    search_fields = ('full_name',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Applicant, ApplicantAdmin)
