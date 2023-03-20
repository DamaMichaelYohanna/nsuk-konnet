from django.urls import path

from . import views

urlpatterns =[
    path("", views.market, name='market place'),
    path("order/place/<int:pk>", views.place_order,  name="place_order"),
    path("product/add", views.add_product, name="add product"),
    path('product/update', views.edit_product, name='update product'),
    path('product/delete', views.delete_product, name='delete product'),
]