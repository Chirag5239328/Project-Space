from rest_framework import serializers
from .models import User, UserAddress, UserPastOrder, Restaurant, Category, RestaurantMenu

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

class UserPastOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPastOrder
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    menu = RestaurantMenuSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = '__all__'
