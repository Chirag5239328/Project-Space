from rest_framework import generics
from .models import User, UserAddress, UserPastOrder, Restaurant, Category, RestaurantMenu
from .serializers import UserSerializer, UserAddressSerializer, UserPastOrderSerializer, RestaurantSerializer, CategorySerializer, RestaurantMenuSerializer

# Views for the User model
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Views for the UserAddress model
class UserAddressListView(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

class UserAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

# Views for the UserPastOrder model
class UserPastOrderListView(generics.ListCreateAPIView):
    queryset = UserPastOrder.objects.all()
    serializer_class = UserPastOrderSerializer

class UserPastOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPastOrder.objects.all()
    serializer_class = UserPastOrderSerializer
class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Views for the Category model
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Views for the RestaurantMenu model
class RestaurantMenuListView(generics.ListCreateAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer

class RestaurantMenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer