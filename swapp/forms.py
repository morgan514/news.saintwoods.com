from django import forms
from .models import PhotoBatchUpload

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleImageField(forms.FileField):
    widget = MultipleFileInput

    def to_python(self, data):
        if not data:
            return []
        if isinstance(data, list):
            return data
        return [data]

    def validate(self, data):
        if not self.required and not data:
            return
        super().validate(data)
        for item in data:
            super().validate(item)

    def run_validators(self, data):
        errors = []
        for item in data:
            try:
                super().run_validators(item)
            except forms.ValidationError as error:
                errors.extend(error.error_list)
        if errors:
            raise forms.ValidationError(errors)

class PhotoBatchUploadForm(forms.ModelForm):
    images = MultipleImageField(required=False)

    class Meta:
        model = PhotoBatchUpload
        fields = []

    def save(self, commit=True):
        instance = super().save(commit=False)
        images = self.cleaned_data.get('images')
        if commit:
            instance.save()  # Save the instance to get an ID
            if images:
                for image in images:
                    PhotoBatchUpload.objects.create(blog_post=instance.blog_post, image=image)
        return instance
