from django.contrib import admin

from core.models import AboutUs, AboutUsInfo, AboutUsStatistic, AboutUsTeam, ContactInfo, ContactPhone, SocialLink, Testimonial

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


class ContactPhoneAdmin(admin.TabularInline):
    model = ContactPhone
    extra = 1


class SocialLinkAdmin(admin.TabularInline):
    model = SocialLink
    extra = 1


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'address')
    inlines = [ContactPhoneAdmin, SocialLinkAdmin]


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
