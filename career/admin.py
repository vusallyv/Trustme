from django.contrib import admin

from career.models import Vacancy

# Register your models here.


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('type',)
    search_fields = ('title', 'short_description', 'full_description')
    exclude = ('slug',)


admin.site.register(Vacancy, VacancyAdmin)
