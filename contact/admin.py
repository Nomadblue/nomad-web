from django.contrib import admin
from contact.models import Contact, PitchContact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message')
    search_fields = ('name', 'phone', 'email', 'message')


class PitchContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'overview')
    search_fields = ('name', 'email', 'overview', 'business_model', 'mvp', 'company_details', 'project_plan', 'dev_calendar', 'middle_person', 'timezone')


admin.site.register(Contact, ContactAdmin)
admin.site.register(PitchContact, PitchContactAdmin)
