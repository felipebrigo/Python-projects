from django.urls import path
from .views import list_products, create_products, update_products, delete_products, MaterialListView

urlpatterns = [
    path('', list_products, name='list_products'),
    path('new', create_products, name='create_products'),
    path('update/<int:id>/', update_products, name='update_products'),
    path('delete/<int:id>/', delete_products, name='delete_products'),
    path('material/', MaterialListView.as_view(), name='MaterialListView'),
    #path('', IndexTemplateView.as_view(), name="indextemplateview"),
]
