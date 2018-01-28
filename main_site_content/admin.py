from django.contrib import admin
from .models import MainSiteContent, Skill, Partner, Service


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1


class PartnerInline(admin.StackedInline):
    model = Partner
    extra = 1


class MainSiteContentAdmin(admin.ModelAdmin):
    class Meta:
        model = MainSiteContent

    inlines = [
        SkillInline,
        ServiceInline,
        PartnerInline,
    ]

    list_display = [
        'name',
        'business_name',
    ]

    fieldsets = (
        ('Site-Wide Content', {
            'fields': (
                'name',
                'business_name',
                'logo',
            )
        }),
        ('Social Profiles', {
            'fields': (
                'facebook_url',
                'twitter_url',
                'dribbble_url',
                'google_plus_url',
                'instagram_url',
            )
        }),
        ('"Home" Section', {
            'fields': (
                'home_background_image',
                'home_header_1',
                'home_header_2',
                'home_header_3',
                'home_paragraph',
                'home_button_text',
                'home_button_link',
            )
        }),
        ('"About" Section', {
            'fields': (
                'about_background_image',
                'about_paragraph',
                'about_quote',
                'about_button_text',
                'about_button_link',
                'about_skills_header',
                'about_skills_footnote',
            )
        }),
        ('"Services" Section', {
            'fields': (
                'services_background_image',
                'services_left_subsection_header',
                'services_middle_subsection_header',
                'services_right_subsection_header',
            )
        }),
        ('"Portfolio" Section', {
            'fields': (
                'portfolio_background_image',
            )
        }),
        ('"Blog" Section', {
            'fields': (
                'blog_background_image',
            )
        }),
        ('"Contact" Section', {
            'fields': (
                'contact_background_image',
                'contact_address_street_1',
                'contact_address_street_2',
                'contact_address_city',
                'contact_address_state_or_province',
                'contact_address_postal_code',
                'contact_address_country',
                'contact_phone',
                'contact_email',
                'contact_footnote',
            )
        })
    )


admin.site.register(MainSiteContent, MainSiteContentAdmin)
