from django.contrib import admin
from .models import Category, Tag, Author, Post, Comment, SocialGroupSidebar, SocialSideBar, EmailSidebar

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)


class EmailSidebarAdmin(admin.StackedInline):
    model = EmailSidebar


class SocialSideBarAdmin(admin.StackedInline):
    model = SocialSideBar


@admin.register(SocialGroupSidebar)
class SocialGroupSideBarAdmin(admin.ModelAdmin):
    inlines = [EmailSidebarAdmin, SocialSideBarAdmin]
