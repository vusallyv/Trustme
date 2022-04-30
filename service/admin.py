from django.contrib import admin

# Register your models here.

from service.models import DigitalAuditAccordion, DigitalAuditApplicant, DigitalAuditInfo, PacketApplicant, ProjectStatistic, ServiceApplicant, ServiceCategory, ServiceAdvantage, ServiceSpecialist, ServiceProject, ServicePacket, Service, ProjectImage, ProjectResult, ProjectProcess


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']


class ServiceAdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class ServiceSpecialistAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class ServiceProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'description', 'cover_image']
    exclude = ['slug']


class ServicePacketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
    exclude = ['slug']


class ProjectImageAdmin(admin.ModelAdmin):
    pass


class ProjectResultAdmin(admin.ModelAdmin):
    list_display = ['title', ]


class ProjectProcessAdmin(admin.ModelAdmin):
    list_display = ['title', ]


class PacketApplicantAdmin(admin.ModelAdmin):
    pass


class ProjectStatisticAdmin(admin.ModelAdmin):
    pass


class ServiceApplicantAdmin(admin.ModelAdmin):
    pass


class DigitalAuditAccordionInline(admin.TabularInline):
    model = DigitalAuditAccordion
    extra = 1


class DigitalAuditInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_active']
    list_filter = ['title', 'is_active']
    inlines = [DigitalAuditAccordionInline]

class DigitalAuditApplicantAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'site_link']
    list_filter = ['full_name', 'phone', 'email', 'site_link']


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceAdvantage, ServiceAdvantageAdmin)
admin.site.register(ServiceSpecialist, ServiceSpecialistAdmin)
admin.site.register(ServiceProject, ServiceProjectAdmin)
admin.site.register(ServicePacket, ServicePacketAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ProjectResult, ProjectResultAdmin)
admin.site.register(ProjectProcess, ProjectProcessAdmin)
admin.site.register(PacketApplicant, PacketApplicantAdmin)
admin.site.register(ProjectStatistic, ProjectStatisticAdmin)
admin.site.register(ServiceApplicant, ServiceApplicantAdmin)
admin.site.register(DigitalAuditInfo, DigitalAuditInfoAdmin)
admin.site.register(DigitalAuditApplicant, DigitalAuditApplicantAdmin)