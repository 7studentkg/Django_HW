"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from post import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.title_page),
    path('product', views.product_view),
    path('create_p', views.product_create),
    path('create_c', views.category_create),
    path('create_r', views.review_create),
    path('category', views.category_view),
    path('product/<int:product_id>/', views.product_datail_view),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),





    # path('hello/', views.hello_world),
    # path('current_date/', views.current_date),
    # path('goodby/', views.goodby )
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
