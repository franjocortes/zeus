from django.forms import ModelForm, TextInput, Select, Textarea, NumberInput

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
            'detail': Textarea(
                attrs={
                    'placeholder': 'Ingrese un detalle para el producto',
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
            'trademark': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price_buy': TextInput(
                attrs={
                    'class': 'form-control text-right'
                }
            ),
            'price_sell_min': TextInput(
                attrs={
                    'class': 'form-control text-right'
                }
            ),
            'price_sell_may': TextInput(
                attrs={
                    'class': 'form-control text-right'
                }
            ),
            'stock': NumberInput(
                attrs={
                    'class': 'form-control text-center'
                }
            )
        }
