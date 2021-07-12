from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog , Contact

# Register your models here.


class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Blog,BlogModelAdmin)

admin.site.register(Contact)
