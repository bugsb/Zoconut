from django.db import models
from django.contrib.auth.models import User

class AccountHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    primary_number = models.IntegerField()
    country_code = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    login_status = models.BooleanField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=20)
    primary_number = models.IntegerField()
    country_code = models.IntegerField()
    basic_info_status = models.BooleanField()
    medical_info_status = models.BooleanField()
    filtering_id = models.ForeignKey(to=AccountHolder, on_delete=models.CASCADE)
    timestamp =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    filtering_id = models.ForeignKey(to=AccountHolder, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=(
        ('confirmed','Confirmed'),
        ('canceled','Canceled')
        )
    )

    payment_date = models.DateField()
    def __str__(self):
        return self.user.name

class Payment(models.Model):
    filtering_id = models.ForeignKey(to=AccountHolder, on_delete=models.CASCADE)
    user = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=20)
    amount = models.IntegerField()
    tax = models.IntegerField()
    paid_amount = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=(
        ('paid','Paid'),
        ('open','Open')
        )
    )
    payment_date = models.DateField(default=None)

    def __str__(self):
        return str(self.filtering_id)

