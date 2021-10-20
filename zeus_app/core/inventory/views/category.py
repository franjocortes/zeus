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
        # context['company'] = CompanyData.objects.get(pk=1).name
        # context['formpage'] = reverse_lazy('inventory:category_new')
        return context


class CategoryCreateView(CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'common/create.html'
    success_url = reverse_lazy('inventory:category_list')