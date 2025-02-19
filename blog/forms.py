from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditor5Widget(attrs={'class': 'django_ckeditor_5'}, config_name='extends')
        }
