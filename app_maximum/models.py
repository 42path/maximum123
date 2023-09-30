from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("Title", max_length=128)
    description = models.TextField("Description")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Auction", help_text="Choose if auction right")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)