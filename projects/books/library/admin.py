# -*- coding: utf-8 -*-

from django.contrib import admin
from library.models import *


class PublisherOfficesInline(admin.TabularInline):
    model = PublisherOffices
    extra = 2


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'print_version', 'publisher')
    list_display_links = ('title',)
    list_editable = ('publisher',)
    list_filter = ('authors', 'publisher', 'publication_date')
    ordering  = ('title',)
    search_fields = ('title', 'authors', 'authors__email')
    date_hierarchy = 'publication_date'

    fieldsets = (
        (None, {
            'fields': ('title', 'authors')
        }),
        ('Выходные данные', {
            'classes': ('collapse',),
            'description': u'Данные об издательстве и издании',
            'fields': ('publisher', 'publication_date'),
        })
    )

    filter_horizontal = ('authors',)
    actions = ['add_new_version',]

    def print_version(self, obj):
        return "издание №%d" % obj.version

    def add_new_version(self, request, queryset):
        for item in queryset:
            item.version += 1
            item.id = None
            item.save(force_insert=True)
    add_new_version.short_description = u"Добавить новое издание"

    def get_actions(self, request):
        actions = super(BookAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

class PublisherAdmin(admin.ModelAdmin):
    inlines = [PublisherOfficesInline,]


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher, PublisherAdmin)
#admin.site.register(PublisherOffices)
