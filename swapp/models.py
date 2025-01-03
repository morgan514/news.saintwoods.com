from django.db import models
from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import ResizeToFit
from django.core.exceptions import ValidationError
import os
from embed_video.fields import EmbedVideoField
from django.utils.html import mark_safe

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Extracts the file extension
    valid_extensions = ['.mp4', '.webm', '.ogg', '.mov', '.avi']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


class BlogPost(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(blank=True)
    image_thumbnail = models.ImageField()
    imageopt = ImageSpecField(source='image_thumbnail',processors=[ResizeToFit(600,600)],
                                           format='JPEG',
                                           options={'quality': 90},
                                           )
    date = models.DateField()
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-rank","-date")


class BlogPostPhoto(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
   
    video = models.FileField(blank=True, validators=[validate_file_extension])
    embed_youtube = EmbedVideoField(blank=True)
    rank = models.IntegerField(default=0)

    class Meta:
        ordering = ("rank","id")

class PhotoBatchUpload(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField()
    imageopt = ImageSpecField(source='image',processors=[ResizeToFit(600,600)],
                                           format='JPEG',
                                           options={'quality': 90},
                                           )
    rank = models.IntegerField(default=0)

    def thumbnail(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return ""
    thumbnail.short_description = 'preview'



    def __str__(self):
        return f"Photo for {self.blog_post.title}"
    class Meta:
        ordering = ("rank","id")