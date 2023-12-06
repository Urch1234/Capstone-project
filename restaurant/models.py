from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.first_name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __self__(self):
        return f'{self.name} : {str(self.price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __self__(self):
        return f"{self.title} : {self.price}"
