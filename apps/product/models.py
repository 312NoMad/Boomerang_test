from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from utils.models import AbstractModel


__all__ = [
    'Product',
    'Review'
]


User = get_user_model()


class Product(AbstractModel):
    name = models.CharField(max_length=255, verbose_name=_('Product name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Product description'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Product price'))
    image = models.ImageField(upload_to='media', verbose_name=_('Product image'), blank=True, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Review(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name=_('Product'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reviews', verbose_name=_('User'))
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name=_('Rating'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return f'{self.product} - {self.rating} - {self.user}'



