from django.contrib import admin
from .models import Team, Social, Info, Avatar, Category, Recruit

admin.site.register(Avatar)
admin.site.register(Recruit)
admin.site.register(Category)


class SocialAdmin(admin.TabularInline):
    model = Social


class InfoAdmin(admin.StackedInline):
    model = Info


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = (InfoAdmin, SocialAdmin)
