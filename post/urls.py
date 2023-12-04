from django.urls import path
from post import views


urlpatterns = [
    path('product', views.product_view),
    path('create_p', views.product_create),
    path('create_c', views.category_create),
    path('create_r', views.review_create),
    path('category', views.category_view),
    path('product/<int:product_id>/', views.product_datail_view),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
]
