from django.db import models

from jewelry.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)

    address = models.CharField('Address', max_length=255, default='', blank=True)
    contact = models.CharField('Contact', max_length=255, default='', blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.id}"

    def get_price(self):
        sum = 0
        for product in self.products.all():
            sum += product.get_price()
        return sum

    def get_count(self):
        count = 0
        for product in self.products.all():
            count += product.quantity
        return count


class OrderProduct(BaseModel):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='products', null=True)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity', default=1)

    class Meta:
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Products'

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'

    def get_price(self):
        return self.product.price * self.quantity
