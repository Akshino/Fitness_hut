from django.urls import path, include
from.import views
from django.contrib import admin
from .views import SellerLoginView



urlpatterns=[
    path('',views.index,name='index'),
    path('customer_dashboard/',views.customer_dashboard,name='customer_dashboard'),
    path('about',views.about,name='about'),
    path('add/', views.product_add, name='product_add'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('products/', views.admin_product_page, name='admin_product_page'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_customer/', views.edit_customer, name='edit_customer'),
    path('address/', views.address_list, name='address_list'),
    path('address/add/', views.address_create, name='address_create'),
    path('address/edit/<int:pk>/', views.address_edit, name='address_edit'),
    path('address/delete/<int:pk>/', views.address_delete, name='address_delete'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.product_search, name='product_search'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('subcategory/<int:subcategory_id>/', views.subcategory_products, name='subcategory_products'),
    path("cart/", views.cart, name="cart"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('delete_item_in_cart/<int:id>/', views.delete_item_in_cart, name='delete_item_in_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('seller_login/', SellerLoginView.as_view(), name='seller_login'),
    path('create_purchase_order/', views.CreatePurchaseOrderView.as_view(), name='create_purchase_order'),
    path('seller/purchase_orders/', views.seller_purchase_orders, name='seller_purchase_orders'),
    path('seller/purchase_order/<int:purchase_order_id>/', views.purchase_order_details, name='purchase_order_details'),
    path('reject_purchase_order/<int:purchase_order_id>/', views.reject_purchase_order, name='reject_purchase_order'),
    path('reports/', views.monthly_sales_report, name='admin_reports'),
    path('similar-products/', views.similar_products, name='similar_products'),
    path('fitness-recommendation/', views.fitness_supplement_recommendation, name='fitness_recommendation'),
    path('visualizations/', views.visualization_view, name='visualizations'),
    path('chat/', views.chat, name='chat'),
]