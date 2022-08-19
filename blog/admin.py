from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.


class PostModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(Post, PostModelAdmin)

