from django.urls import path
from .views import list_products, create_products, update_products, delete_products, login_user, IndexTemplateView,submit_login, logout_user, create_contracts, delete_contracts, update_contracts, list_contract
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),
    path('login/', login_user, name='login_user'),
    path('login/submit', submit_login),
    path('logout/', logout_user, name='logout_user'),
    path('index/', IndexTemplateView.as_view(), name="index"),
    path('newproduct/', create_products, name='create_products'),
    path('updateproduct/<int:id>/', update_products, name='update_products'),
    path('deleteproduct/<int:id>/', delete_products, name='delete_products'),
    path('productlist/', list_products, name='list_products'),

    path('newcontract/', create_contracts, name='create_contracts'),
    path('updatecontract/<int:id>/', update_contracts, name='update_contracts'),
    path('deletecontract/<int:id>/', delete_contracts, name='delete_contracts'),
    path('contractlist/', list_contract, name='list_contract'),

]

'''
    #from django.views import ProductListView, IndexTemplateView, ProductUpdateView, ProductDeleteView, ProductCreateView
    path('', IndexTemplateView.as_view(), name="index"),
    path('create/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('productlist/', ProductListView.as_view(), name='ProductListView'),
    path('productupdate/<pk>', ProductUpdateView.as_view(), name='ProductUpdateView'),
    path('productdelete/<pk>/', ProductDeleteView.as_view(), name='ProductDeleteView'),
'''