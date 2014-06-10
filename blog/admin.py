from django.contrib import admin

from blog.models import NomadPost


class NomadPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'pub_date', 'slug', 'summary')
    list_editable = ('pub_date',)
    search_fields = ('title', 'summary')
    fields = ('bloguser', 'pub_date', 'status', 'title', 'slug', 'summary', 'content', 'categories')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(NomadPost, NomadPostAdmin)
