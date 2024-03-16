from django.contrib import admin

from .models import Blog, Tag, Thought, Contact

# Register your models here.
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Thought)

class BlogAdmin(admin.ModelAdmin):
	list_display = ("title", "sub_title", "date_published")
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
