from django.contrib import admin

# Register your models here.

from portfolio.brief.website.models import Brief, BriefPhoto


class BriefAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': [
         'full_name', 'email', 'phone', 'phone_prefix']}),
        ('General Information', {'fields': [
         'company_name', 'activity_sphere', 'website_url', 'new_domain', 'rival_website', 'liked_website']}),
        ('Service Information', {'fields': [
         'project_period', 'design', 'website_type', 'requirements', 'language']}),
    ]


class BriefPhotoInline(admin.TabularInline):
    model = BriefPhoto
    extra = 1


admin.site.register(Brief, BriefAdmin)
