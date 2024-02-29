from django.contrib import admin

from content.models import Product, Lesson, Group


class LessInline(admin.TabularInline):
    model = Lesson



@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title',]


@admin.register(Product)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessInline]
    list_display = ['title', 'price', 'started_at', ]
    list_filter = ['started_at', 'price']
    search_fields = ['title',]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', ]