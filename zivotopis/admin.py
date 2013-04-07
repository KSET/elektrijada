from django.contrib import admin
from zivotopis.models import CurriculumVitae

class CVAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'created', 'college', 'course')
    search_fields = ('last_name', 'first_name', 'created', 'college', 'course')

    list_filter = ['created']
    date_hierarchy = 'created'

    ordering = ['-created']

admin.site.register(CurriculumVitae, CVAdmin)
