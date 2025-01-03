from django.contrib import admin
from .models import BlogPost, BlogPostPhoto,PhotoBatchUpload
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from .forms import PhotoBatchUploadForm

class PhotoBatchUploadInline(admin.TabularInline):
    model = PhotoBatchUpload
    form = PhotoBatchUploadForm
    extra = 1
    fields = ['images','thumbnail']
    readonly_fields = [ 'thumbnail']




class BlogPostPhotoInline(SortableInlineAdminMixin, admin.StackedInline):
    model = BlogPostPhoto
    list_display = ('id',)
    verbose_name = "Blog Post Video"
    verbose_name_plural = "Blog Post Videos"
    extra = 1  

class BlogPostAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'rank', 'title', 'slug', 'date')
    inlines = [
        BlogPostPhotoInline,
        PhotoBatchUploadInline
    ]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(BlogPost, BlogPostAdmin)


