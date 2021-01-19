from django.urls import path
from .views import list_products, create_products, update_products, delete_products, login_user, IndexTemplateView
from django.views.generic import RedirectView




urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),
    path('login/', login_user, name='login_user'),
    path('index/', IndexTemplateView.as_view(), name="index"),
    path('newproduct', create_products, name='create_products'),
    path('updateproduct/<int:id>/', update_products, name='update_products'),
    path('deleteproduct/<int:id>/', delete_products, name='delete_products'),
    path('productlist/', list_products, name='list_products'),

]

'''
    #from django.views import ProductListView, IndexTemplateView, ProductUpdateView, ProductDeleteView, ProductCreateView
    path('', IndexTemplateView.as_view(), name="index"),
    path('create/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('productlist/', ProductListView.as_view(), name='ProductListView'),
    path('productupdate/<pk>', ProductUpdateView.as_view(), name='ProductUpdateView'),
    path('productdelete/<pk>/', ProductDeleteView.as_view(), name='ProductDeleteView'),
'''