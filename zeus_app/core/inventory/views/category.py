from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from core.inventory.forms import CategoryForm
from core.inventory.models import Categories


class CategoryListView(ListView):
    template_name = 'category/list.html'
    model = Categories

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categorías'
        context['title2'] = 'Listado'
        context['title_form'] = 'Categoria'
        context['form'] = CategoryForm()
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
                for i in Categories.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                form = CategoryForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'upd':
                cat = Categories.objects.get(pk=request.POST['id'])
                print(cat)
                cat.name = request.POST['name']
                cat.save()
            elif action == 'del':
                category = Categories.objects.get(pk=request.POST['id'])
                category.delete()
            else:
                data['error'] = 'Action invalid'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
