from django.forms.widgets import ClearableFileInput

class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

    def render(self, name, value, attrs=None, renderer=None):
        attrs['multiple'] = 'multiple'
        return super().render(name, value, attrs=attrs, renderer=renderer)

from django import forms
from .models import PhotoBatchUpload
from .widgets import MultipleFileInput

class PhotoBatchUploadForm(forms.ModelForm):
    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = PhotoBatchUpload
        fields = ['images']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'images' in self.files:
            for image in self.files.getlist('images'):
                PhotoBatchUpload.objects.create(blog_post=instance.blog_post, image=image)
        return instance
