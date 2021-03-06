from django.contrib import admin

from .models import ChargeRate, Client, ContactPhone, ContactEmail, Contact, \
                    Profile
from core.models import ActivityCode


admin.site.register(ChargeRate)
admin.site.register(Client)
admin.site.register(ContactPhone)
admin.site.register(ContactEmail)

class ContactPhoneInline(admin.TabularInline):
    model = ContactPhone

class ContactEmailInline(admin.TabularInline):
    model = ContactEmail

class ContactAdmin(admin.ModelAdmin):
    inlines = (ContactPhoneInline, ContactEmailInline,)
admin.site.register(Contact, ContactAdmin)


class ContactInline(admin.TabularInline):
    model = Contact
    
class ChargeRateInline(admin.TabularInline):
    model = ChargeRate

class ActivityCodeInline(admin.TabularInline):
    model = ActivityCode

class ProfileAdmin(admin.ModelAdmin):
    inlines = (ChargeRateInline, ActivityCodeInline, ContactInline)
admin.site.register(Profile, ProfileAdmin)
