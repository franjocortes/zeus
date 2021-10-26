from django.forms import ModelForm, TextInput

from core.inventory.models import Categories, Trademarks, Products


class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['autocomplete'] = 'off'

        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Categories
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la categoría',
                    'class': 'form-control'
                }
            ),
        }


class TrademarkForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['autocomplete'] = 'off'

        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Trademarks
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la marca',
                    'class': 'form-control'
                }
            ),
        }


class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['autocomplete'] = 'off'

        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Products
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del producto',
                    'class': 'form-control'
                }
            ),
        }