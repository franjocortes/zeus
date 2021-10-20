from django.urls import path
from core.inventory.views.category import CategoryListView

app_name = 'inventory'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
]