from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from utils.models import AbstractModel

from apps.product.models import Product


__all__ = [
    'Order',
    'OrderItem',
    'Cart',
    'CartItem'
]


User = get_user_model()


ORDER_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('pending', 'Pending'),
    ('done', 'Done')
)


class Order(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=20, default='draft', verbose_name='Order Status')
    description = models.TextField(blank=True, null=True,verbose_name=_('Order Description'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'Order {self.id} - {self.user}'

    @property
    def total_cost(self):
        return sum(item.cost for item in self.order_items.all())


class OrderItem(AbstractModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', verbose_name=_('Order'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item', verbose_name=_('Product'))
    quantity = models.PositiveIntegerField()

    @property
    def cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'


class Cart(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', verbose_name=_('User'))

    @property
    def total_cost(self):
        return sum(item.cost for item in self.cart_items.all())


class CartItem(AbstractModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name=_('Cart'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item', verbose_name=_('Product'))
    quantity = models.PositiveIntegerField()

    @property
    def cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.name} - {self.quantity} - {self.cost}'
