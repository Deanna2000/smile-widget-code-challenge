from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25, help_text='Customer facing name of product')
    code = models.CharField(max_length=10, help_text='Internal facing reference to product')
    price = models.PositiveIntegerField(help_text='Price of product in cents')

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)


class GiftCard(models.Model):
    code = models.CharField(max_length=30)
    amount = models.PositiveIntegerField(help_text='Value of gift card in cents')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.code, self.formatted_amount)

    @property
    def formatted_amount(self):
        return '${0:.2f}'.format(self.amount / 100)

class ProductPrice(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	sale_price = models.PositiveIntegerField(help_text='Price of product in cents')
	sale_date_start = models.DateField(help_text='Start of sale pricing')
	sale_date_end = models.DateField(blank=True, null=True, help_text='End of sale pricing')

	def __str__(self):
		return '{} - {}'.format(self.product.name, self.sale_date_start)

