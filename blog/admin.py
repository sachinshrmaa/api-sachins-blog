from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import Group
from .models import BlogPost



class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.unregister(Group)


#Dashboard Styling
admin.site.site_header = "Sachins Blog"
admin.site.site_title = "Sachins Blog"
admin.site.index_title = "Blog Database"
