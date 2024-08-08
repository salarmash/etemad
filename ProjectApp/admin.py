from django.contrib import admin
from .models import Category, Project, Intro, Descriptions, Avatar, Detail, Gallery, Resume, Benefit, BenefitItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("category_slug",)


class IntroAdmin(admin.StackedInline):
    model = Intro


class DescriptionAdmin(admin.StackedInline):
    model = Descriptions


class AvatarAdmin(admin.StackedInline):
    model = Avatar


class DetailAdmin(admin.StackedInline):
    model = Detail
    extra = 1


class GalleryAdmin(admin.TabularInline):
    model = Gallery
    extra = 3
    exclude = ("alt",)


class ResumeAdmin(admin.StackedInline):
    model = Resume
    exclude = ("name", "role", "text")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (IntroAdmin, DescriptionAdmin, AvatarAdmin, GalleryAdmin, DetailAdmin, ResumeAdmin)


class BenefitItemAdmin(admin.StackedInline):
    model = BenefitItem
    extra = 1


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    inlines = (BenefitItemAdmin,)
