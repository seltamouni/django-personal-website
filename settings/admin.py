from django.contrib import admin
from .models import About

from django_summernote.admin import SummernoteModelAdmin


class AboutModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(About,AboutModelAdmin)

