from django.urls import path
from core.inventory.views.category import CategoryListView
from core.inventory.views.trademark import TrademarkListView
from core.inventory.views.product import ProductListView

app_name = 'inventory'


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('trademarks/', TrademarkListView.as_view(), name='trademark_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
]