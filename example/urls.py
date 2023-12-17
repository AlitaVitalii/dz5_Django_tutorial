from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('2', views.list_example, name='index-2'),
    path('product/<int:pk>/delete', views.ProductDeleteViews.as_view(), name='product-delete'),

    path('examstatic/', views.static_example_view, name='examstatic'),
]
