from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)  # Assuming password hashes are 128 characters long
    address = models.TextField()  # You can adjust this to CharField if needed
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.username

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.username}'s Address"

class UserPastOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.PositiveIntegerField()  # Assuming a numeric ID
    restaurant_name = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Example for monetary values
    
    def __str__(self):
        return f"{self.user.username}'s Order at {self.restaurant_name}"

class Restaurant(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # Assuming ratings like 3.9
    image_url = models.URLField()  # You can adjust this based on your needs
    cuisine = models.CharField(max_length=100,default='MultiCuisine')  # Added cuisine field

class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)

class RestaurantMenu(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Example for monetary values
    image_url = models.URLField()  # You can adjust this based on your needs
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # Assuming ratings like 4.2

