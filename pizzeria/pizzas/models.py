from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza that the user will describe"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns string representation of model"""
        return self.name


class Topping(models.Model):
    """Specific topping on a pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        """Returns string representation of model"""
        return self.name