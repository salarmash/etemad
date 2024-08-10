from django.contrib import admin
from .models import Service, Gallery, Description, Description2, DescriptionList, SideBarItem, SideBarCounter, \
    SideBarContent, \
    FAQSection, FAQItem, VisionsSection, VisionItem, Feature, FeatureItem, AboutSection, AboutList, Contact, \
    ContactEmail, ContactPhone, ContactAddress, SideBar


class GalleryAdmin(admin.TabularInline):
    model = Gallery
    extra = 1


class DescriptionAdmin(admin.StackedInline):
    model = Description
    extra = 1


class Description2Admin(admin.StackedInline):
    model = Description2
    extra = 1


class DescriptionListAdmin(admin.StackedInline):
    model = DescriptionList
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    inlines = (DescriptionAdmin, Description2Admin, GalleryAdmin, DescriptionListAdmin)


class SidebarContentAdmin(admin.StackedInline):
    model = SideBarContent
    extra = 1


@admin.register(SideBarCounter)
class SideBarCounterAdmin(admin.ModelAdmin):
    extra = 3


@admin.register(SideBarItem)
class SidebarAdmin(admin.ModelAdmin):
    model = SideBarItem
    inlines = (SidebarContentAdmin,)


class FaqItemAdmin(admin.StackedInline):
    model = FAQItem
    extra = 1


@admin.register(FAQSection)
class FAQAdmin(admin.ModelAdmin):
    model = FAQSection
    inlines = (FaqItemAdmin,)


class VisionItemAdmin(admin.StackedInline):
    model = VisionItem
    extra = 1


@admin.register(VisionsSection)
class VisionAdmin(admin.ModelAdmin):
    model = VisionsSection
    inlines = (VisionItemAdmin,)


class FeatureItemAdmin(admin.StackedInline):
    model = FeatureItem
    extra = 1


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    model = Feature
    inlines = (FeatureItemAdmin,)


class AboutListAdmin(admin.StackedInline):
    model = AboutList
    extra = 1


@admin.register(AboutSection)
class AboutAdmin(admin.ModelAdmin):
    model = AboutSection
    inlines = (AboutListAdmin,)
    exclude = ("image_alt", "avatar_name")


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


admin.site.register(SideBar)
