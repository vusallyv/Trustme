from django.contrib import admin

# Register your models here.

from service.models import Category, Advantage, Specialist, Project, Packet, Service


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'description', 'image']
    exclude = ['slug']


class PacketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
    exclude = ['slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Packet, PacketAdmin)
admin.site.register(Service, ServiceAdmin)
