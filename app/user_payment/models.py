from django.conf import settings
from django.db import models
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY_TEST


class Item(models.Model):
    class Meta:
        verbose_name_plural = 'Товар'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField()


class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_id = models.CharField(max_length=50, blank=True, null=True)

    def calculate_total_cost(self):
        total_cost = sum([item.price for item in self.items.all()])
        self.total_cost = total_cost
        self.save()

    def process_payment(self, token):
        charge = stripe.Charge.create(
            amount=int(self.total_cost * 100),
            currency="usd",
            source=token,
            description="Payment for order #" + str(self.id)
        )
        self.stripe_payment_id = charge.id
        self.save()
