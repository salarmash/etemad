from django.contrib import admin
from .models import Award, AwardItems, Testimonial, TestItems, Service, ServiceItem, Contact, Signature, Company, \
    Company2, CompanyImage, Company2Image, Process, Partner, AllProcess, Group


class AwardItemAdmin(admin.StackedInline):
    model = AwardItems


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    inlines = [AwardItemAdmin, ]


class TestItemsAdmin(admin.StackedInline):
    model = TestItems


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    inlines = (TestItemsAdmin,)


class ServiceItemAdmin(admin.StackedInline):
    model = ServiceItem


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceItemAdmin, ]


admin.site.register(Contact)
admin.site.register(Signature)


class ImageAdmin(admin.TabularInline):
    model = CompanyImage


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,)


class Image2Admin(admin.TabularInline):
    model = Company2Image


@admin.register(Company2)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (Image2Admin,)


class ProcessAdmin(admin.StackedInline):
    model = Process
    extra = 3

    def has_add_permission(self, request, obj=None):
        if obj and self.model.objects.filter(
                group=obj).count() >= 3:  # Assuming 'parent' is a ForeignKey to the related model
            return False
        return super().has_add_permission(request, obj)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (ProcessAdmin,)


admin.site.register(AllProcess)
admin.site.register(Partner)
