from django.http import JsonResponse
from django.views.generic import ListView

from core.inventory.forms import ProductForm
from core.inventory.models import Products


class ProductListView(ListView):
    template_name = 'product/list.html'
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['title2'] = 'Listado'
        context['title_form'] = 'Producto'
        context['form'] = ProductForm()
        context['type_form'] = 'basic'
        # context['company'] = CompanyData.objects.get(pk=1).name
        # context['formpage'] = reverse_lazy('inventory:category_new')
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Products.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                form = ProductForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'upd':
                cat = Products.objects.get(pk=request.POST['id'])
                cat.name = request.POST['name']
                cat.save()
            elif action == 'del':
                category = Products.objects.get(pk=request.POST['id'])
                category.delete()
            elif action == 'reset':
                if int(request.POST['id']) > 0:
                    product = Products.objects.get(pk=request.POST['id'])
                    data = [product.toJSON()]
                else:
                    data = [{
                        'price_sell_min': 0.0,
                        'price_sell_may': 0.0,
                    }]
            else:
                data['error'] = 'Action invalid'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
