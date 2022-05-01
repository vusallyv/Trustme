from django.contrib import admin

from core.models import AboutUs, AboutUsInfo, AboutUsStatistic, AboutUsTeam, Testimonial

# Register your models here.


class AboutUsTeamInline(admin.TabularInline):
    model = AboutUsTeam
    extra = 1


class AboutUsInfoInline(admin.TabularInline):
    model = AboutUsInfo
    extra = 1


class AboutUsStatisticInline(admin.TabularInline):
    model = AboutUsStatistic
    extra = 1


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [AboutUsTeamInline, AboutUsInfoInline, AboutUsStatisticInline]


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'comment')
    list_filter = ('full_name', 'position', 'comment')
    search_fields = ('full_name', 'position', 'comment')


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
