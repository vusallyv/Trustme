from django.contrib import admin

# Register your models here.

from portfolio.models import ProjectImage, ProjectProcess, ProjectResult, ProjectStatistic, ServiceProject


class ServiceProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'description', 'cover_image']
    exclude = ['slug']


class ProjectImageAdmin(admin.ModelAdmin):
    pass


class ProjectResultAdmin(admin.ModelAdmin):
    list_display = ['title', ]


class ProjectProcessAdmin(admin.ModelAdmin):
    list_display = ['title', ]


class ProjectStatisticAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceProject, ServiceProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ProjectResult, ProjectResultAdmin)
admin.site.register(ProjectProcess, ProjectProcessAdmin)
admin.site.register(ProjectStatistic, ProjectStatisticAdmin)
