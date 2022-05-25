from django.contrib import admin

# Register your models here.

from service.models import Applicant, ServiceCategory, ServiceAdvantage, ServiceSpecialist, ServicePacket, Service


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']


class ServiceAdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class ServiceSpecialistAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class ServicePacketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
    exclude = ['slug']


class ApplicantAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceAdvantage, ServiceAdvantageAdmin)
admin.site.register(ServiceSpecialist, ServiceSpecialistAdmin)
admin.site.register(ServicePacket, ServicePacketAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Applicant, ApplicantAdmin)
