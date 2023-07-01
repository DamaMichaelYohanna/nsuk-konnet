from django.urls import path

from . import views

urlpatterns =[
    path("products", views.market, name='market place'),
    path("product/<int:pk>/detail", views.product_detail, name='product-detail'),
    path("order/place/<int:pk>", views.place_order,  name="place_order"),
    path("order/customer/", views.view_order_by_customer, name="view orders"),
    # for sellers
    path("product/add", views.add_product, name="add product"),
    path('product/update', views.edit_product, name='update product'),
    path('product/delete', views.delete_product, name='delete product'),
]