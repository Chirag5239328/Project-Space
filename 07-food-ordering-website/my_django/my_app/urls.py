from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('addresses/', views.UserAddressListView.as_view(), name='address-list'),
    path('addresses/<int:pk>/', views.UserAddressDetailView.as_view(), name='address-detail'),
    path('orders/', views.UserPastOrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.UserPastOrderDetailView.as_view(), name='order-detail'),
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('menus/', views.RestaurantMenuListView.as_view(), name='menu-list'),
    path('menus/<int:pk>/', views.RestaurantMenuDetailView.as_view(), name='menu-detail'),
]
