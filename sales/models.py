from django.db import models
from django.urls import reverse
# from django.utils import timezone


class Sale(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Цена')
    prime_price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Основная цена')
    date = models.DateField(verbose_name='Дата продажи')

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return 'Продажа #%s от %s' % (self.id, self.date)

    def diff_price(self):
        return self.price - self.prime_price

    diff_price.short_description = 'Разность цен'

    def get_absolute_url(self):
        return reverse('sales:object_detail', args=[self.id])
