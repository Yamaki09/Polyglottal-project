from django.contrib import admin
from createpost.models import CreatePost

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(CreatePost, PostAdmin)
