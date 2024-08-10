from django.contrib import admin
from .models import Hero, HeroItem, About, Avatar, AboutItems, Idea, IdeaItem, Service, ServiceItem, Advantage, \
    AdvantageItem, HowWeWork, WorkItem, Core, CoreItem


class HeroItemAdmin(admin.StackedInline):
    model = HeroItem
    extra = 1


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = (HeroItemAdmin,)


class AboutItemsAdmin(admin.StackedInline):
    model = AboutItems
    extra = 3


class AvatarAdmin(admin.StackedInline):
    model = Avatar
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = (AvatarAdmin, AboutItemsAdmin)
    exclude = ("image_alt",)


class IdeaItemAdmin(admin.StackedInline):
    model = IdeaItem


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    inlines = (IdeaItemAdmin,)


class ServiceItemAdmin(admin.StackedInline):
    model = ServiceItem


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceItemAdmin,)


class AdvantageItemAdmin(admin.StackedInline):
    model = AdvantageItem
    extra = 1


@admin.register(Advantage)
class ServiceAdmin(admin.ModelAdmin):
    inlines = (AdvantageItemAdmin,)


class WorkItemAdmin(admin.StackedInline):
    model = WorkItem
    extra = 1


@admin.register(HowWeWork)
class HowWeWorkAdmin(admin.ModelAdmin):
    inlines = (WorkItemAdmin,)


class CoreItemAdmin(admin.StackedInline):
    model = CoreItem
    extra = 2


@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    inlines = (CoreItemAdmin,)
