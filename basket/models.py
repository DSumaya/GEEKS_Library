from django.db import models
from library.models import Books


class BasketModel(models.Model):
    PAYMENT_METHOD = [
        ('Mbank', 'Mbank'),
        ('Optima', 'Optima'),
        ('Visa', 'Visa')
    ]
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='basket')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    pay = models.CharField(choices=PAYMENT_METHOD, max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.book.title}  {self.quantity} - {self.total_price}"
