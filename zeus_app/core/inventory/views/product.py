from django.views.generic import ListView

from core.inventory.models import Products


class CategoryListView(ListView):
    template_name = 'category/list.html'
    model = Products

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