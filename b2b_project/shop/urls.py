from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [ 
    path('', views.home, name = 'home'),
    path('admin-dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
    path('admin-dashboard/profile/', views.admin_profile, name = 'admin_profile'),
    path('admin-dashboard/profile/<str:edit>/', views.admin_profile, name = 'admin_profile_edit'),
    path('admin-dashboard/product-list/', views.product_list, name = 'product_list'),
    path('admin-dashboard/product/<int:id>/', views.product_detail, name = 'product_detail'),
    path('admin-dashboard/add-product/', views.add_product, name = 'add_product'),
    path('admin-dashboard/customer-list/', views.list_customer, name = 'customer_list'),
    path('admin-dashboard/customer-requests/', views.customer_requests, name = 'customer_requests'),
    path('admin-dashboard/salesman-list/', views.list_customer, name = 'salesman_list'),
    path('admin-dashboard/add-salesman/', views.list_customer, name = 'add_salesman'),
]