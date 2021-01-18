from django.urls import path
from .views import list_products, create_products, update_products, delete_products, ProductListView, IndexTemplateView, ProductUpdateView, ProductDeleteView, ProductCreateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('create/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('productlist/', ProductListView.as_view(), name='ProductListView'),
    path('productupdate/<pk>', ProductUpdateView.as_view(), name='ProductUpdateView'),
    path('productdelete/<pk>/', ProductDeleteView.as_view(), name='ProductDeleteView'),
    path('new', create_products, name='create_products'),
    path('update/<int:id>/', update_products, name='update_products'),
    path('delete/<int:id>/', delete_products, name='delete_products'),
    path('product/', list_products, name='list_products'),

]
