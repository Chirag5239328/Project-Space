from django.contrib import admin
from .models import User, UserAddress, UserPastOrder, Restaurant, Category, RestaurantMenu

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserPastOrder)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(RestaurantMenu)