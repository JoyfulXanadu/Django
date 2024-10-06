from django import forms
from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data.lower() in ProductForm.forbidden_words:
            raise forms.ValidationError(f'Содержит запрещенное слово: {cleaned_data}. Введите другое имя продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in ProductForm.forbidden_words:
            raise forms.ValidationError(f'Содержит запрещенное слово: {cleaned_data}. Введите другое описание продукта')
        return cleaned_data


class ProductVersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_active', 'description', 'category')
