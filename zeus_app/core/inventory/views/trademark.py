from django.http import JsonResponse
from django.views.generic import ListView

from core.inventory.forms import TrademarkForm
from core.inventory.models import Trademarks


class TrademarkListView(ListView):
    template_name = 'trademark/list.html'
    model = Trademarks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Marcas'
        context['title2'] = 'Listado'
        context['title_form'] = 'Marca'
        context['form'] = TrademarkForm()
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
                for i in Trademarks.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                form = TrademarkForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'upd':
                cat = Trademarks.objects.get(pk=request.POST['id'])
                print(cat)
                cat.name = request.POST['name']
                cat.save()
            elif action == 'del':
                category = Trademarks.objects.get(pk=request.POST['id'])
                category.delete()
            else:
                data['error'] = 'Action invalid'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
