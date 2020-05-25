from django.db import models
from django.contrib.auth.models import User

DEFAULT_ITEM = ('Consulting Charges')
DEFAULT_SELL_PRICE_FOR_CONSULTING = 200
# Code added in 0004_auto_20200525_1105.py file of migrations folder to automatically generate default item.

# Create your models here.
class items(models.Model):
	item_name = models.CharField(max_length=50)
	cost_price = models.IntegerField(blank=True, null=True)
	sell_price = models.IntegerField(blank=True, null=True)
	manufacturer = models.CharField(max_length=50, null=True, blank=True)
	description = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.item_name

class stock(models.Model):
	item = models.ForeignKey(items, on_delete=models.CASCADE, related_name='stock_item')
	quantity = models.IntegerField()
	purchase_date = models.DateField()
	expiry_date = models.DateField()

	def __str__(self):
		return self.item.item_name
