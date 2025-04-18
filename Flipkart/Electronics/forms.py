from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and hasattr(image, 'content_type'):  # Only validate new uploads
            if image.size > 2 * 1024 * 1024:  # 2MB limit
                raise forms.ValidationError("Image file too large ( > 2MB )")
            if not image.content_type.startswith('image/'):
                raise forms.ValidationError("File is not an image")
        return image

