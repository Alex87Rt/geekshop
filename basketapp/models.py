from django.db import models
from authapp.models import User
from mainapp.models import Product

#
# class BasketQuerySet(models.QuerySet):
#     def delete(self):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#         super().delete()
#

class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category').select_related()

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)
    #
    # def delete(self, **kwargs):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete()
