from django.urls import path
from core.inventory.views.category import CategoryListView
from core.inventory.views.trademark import TrademarkListView

app_name = 'inventory'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('trademarks/', TrademarkListView.as_view(), name='trademark_list'),
]