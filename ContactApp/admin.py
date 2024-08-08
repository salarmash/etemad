from django.contrib import admin
from .models import Contact, ContactPhone, ContactAddress, ContactEmail, ContactForm


class PhoneAdmin(admin.TabularInline):
    model = ContactPhone
    extra = 1


class EmailAdmin(admin.StackedInline):
    model = ContactEmail
    extra = 1


class AddressAdmin(admin.StackedInline):
    model = ContactAddress
    extra = 1


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    inlines = (PhoneAdmin, EmailAdmin, AddressAdmin)


admin.site.register(ContactForm)
