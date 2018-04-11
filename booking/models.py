from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vehicle.models import Vehicle

# Create your models here.
class Book(models.Model):
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    bookingDate=models.DateTimeField(default=timezone.now)
    startDate=models.DateTimeField("Start date ")
    endDate=models.DateTimeField("end date ")
    securityDeposit=models.IntegerField()
    status_CHOICES=(
        ('B','booked'),
        ('NB','not booked')
    )
    status=models.CharField(
        max_length=2,
        choices=status_CHOICES,
        default='NB',
    )
    discountId=models.CharField(max_length=100)
    allottedUser=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    def __str__(self):
        return 'source : '+self.source