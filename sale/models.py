from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=255)
    credit = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name


class SaleOrder(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    phone = models.CharField(max_length=11)
    amount = models.PositiveIntegerField()


class Transaction(models.Model):    
    STATUS_COMPLETED='COM'
    STATUS_FAILED='FAI'
    STATUS_PENDING = 'PEN'

    STATUS_CHOICES=[
        (STATUS_COMPLETED,'Completed'),
        (STATUS_FAILED,'Failed'),
        (STATUS_PENDING,'Pending')
    ]

    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.IntegerField()
    status=models.CharField(max_length=3,choices=STATUS_CHOICES,default=STATUS_PENDING)



class Order(models.Model):
    TYPE_DEPOSIT = 'DEP'
    TYPE_WITHDRAW = 'WIT'

    STATUS_COMPLETED='COM'
    STATUS_FAILED='FAI'
    STATUS_PENDING = 'PEN'

    TYPE_CHOICES = [
        (TYPE_DEPOSIT, 'Deposit'),
        (TYPE_WITHDRAW, 'Withdraw')
    ]

    STATUS_CHOICES=[
        (STATUS_COMPLETED,'Completed'),
        (STATUS_FAILED,'Failed'),
        (STATUS_PENDING,'Pending')
    ]

    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    status=models.CharField(max_length=3,choices=STATUS_CHOICES,default=STATUS_PENDING)

    class Meta:
        abstract = True



class CreditOrder(Order): 
    order_type = models.CharField(
        max_length=3, choices=Order.TYPE_CHOICES, default=Order.TYPE_DEPOSIT)
  