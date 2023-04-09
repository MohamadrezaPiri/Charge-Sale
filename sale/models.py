from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=255)
    credit = models.IntegerField()

    def __str__(self):
        return self.name


class SaleOrder(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    phone = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()


class Transaction(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.IntegerField()
    type=models.CharField(max_length=3)


class CreditOrder(models.Model):
    TYPE_DEPOSIT = 'DEP'
    TYPE_WITHDRAW = 'WIT'

    TYPE_CHOICES = [
        (TYPE_DEPOSIT, 'Deposit'),
        (TYPE_WITHDRAW, 'Withdraw')
    ]

    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    order_type = models.CharField(
        max_length=3, choices=TYPE_CHOICES, default=TYPE_DEPOSIT)
