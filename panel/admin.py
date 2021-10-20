from django.contrib import admin
from panel.models import Friend, Markdown
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

admin.site.register(Friend)
admin.site.register(Markdown,MarkdownxModelAdmin)
