from django import forms

from post.models import Product, Category, Review

class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length= 200)
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    rate = forms.FloatField(min_value=1, max_value=10)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="------", required=False, initial=None)
    # Позволяет выбрать категорию продукта который уже существует ( поле не обязательное )


    def clean_content(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if len(content) < 30:
            raise forms.ValidationError("Content to short!")
        if not content:
            raise forms.ValidationError("Content is rewuired!")

        return cleaned_data

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['post', 'text']
        widgets = {'text': forms.Textarea(),}
