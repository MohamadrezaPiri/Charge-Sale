from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=255)
    credit = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name


class SaleOrder(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    phone = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()


class Transaction(models.Model):
    TYPE_DEPOSIT = 'DEP'
    TYPE_WITHDRAW = 'WIT'
    TYPE_SALE = 'SALE'

    STATUS_COMPLETED='COM'
    STATUS_FAILED='FAI'

    TYPE_CHOICES = [
        (TYPE_DEPOSIT, 'Deposit'),
        (TYPE_WITHDRAW, 'Withdraw'),
        (TYPE_SALE, 'Sale')
    ]

    STATUS_CHOICES=[
        (STATUS_COMPLETED,'Completed'),
        (STATUS_FAILED,'Failed')
    ]


    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    type=models.CharField(max_length=4,choices=TYPE_CHOICES,default=TYPE_SALE)
    status=models.CharField(max_length=3,choices=STATUS_CHOICES,default=STATUS_COMPLETED)


class CreditOrder(models.Model): 
    TYPE_DEPOSIT = 'DEP'
    TYPE_WITHDRAW = 'WIT'

    STATUS_COMPLETED='COM'
    STATUS_FAILED='FAI'

    TYPE_CHOICES = [
        (TYPE_DEPOSIT, 'Deposit'),
        (TYPE_WITHDRAW, 'Withdraw')
    ]

    STATUS_CHOICES=[
        (STATUS_COMPLETED,'Completed'),
        (STATUS_FAILED,'Failed')
    ]

    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    order_type = models.CharField(
        max_length=3, choices=TYPE_CHOICES, default=TYPE_DEPOSIT)
    status=models.CharField(max_length=3,choices=STATUS_CHOICES,default=STATUS_COMPLETED)
