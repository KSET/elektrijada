from django.contrib import admin
from zivotopis.models import CurriculumVitae


class CVAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'created', 'college', 'course', 'visible')
    search_fields = ('last_name', 'first_name', 'created', 'college', 'course')

    list_filter = ['visible', 'created']
    date_hierarchy = 'created'

    ordering = ['-created']

    actions = ['make_visible', 'make_invisible']

    def make_visible(self, request, queryset):
        queryset.update(visible=True)
    make_visible.short_description = 'Set selected cvs as Visible'

    def make_invisible(self, request, queryset):
        queryset.update(visible=False)
    make_invisible.short_description = 'Set selected cvs as Not Visible'

admin.site.register(CurriculumVitae, CVAdmin)
