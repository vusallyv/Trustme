from django.contrib import admin

from core.models import AboutUs, AboutUsInfo, AboutUsStatistic, AboutUsTeam, Applicant, Contact, Testimonial, Vacancy

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


admin.site.register(Contact, ContactAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
