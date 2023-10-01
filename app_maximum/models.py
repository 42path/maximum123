from django.db import models
from django.contrib import admin
from django.utils.html import *

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("Title", max_length=128)
    description = models.TextField("Description")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Auction", help_text="Choose if auction right")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    @admin.display(description='Date_build')
    def create_date(self):
        from django.utils import timezone
        if self.create_date.date() == timezone.now().date:
            create_time = self.create_at.time().strftime("%H:%M:%S")
            return format_html(
            '<span style="color: green; font-weight: bold;">Today in {}</span>', create_time
        )
        return self.create_at.strftime("%d.%m.%Y" in "%H:%M:%S")