from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.addresses.models import Address


class User(AbstractUser):
    first_name = models.CharField(max_length=55, blank=False, null=False)
    last_name = models.CharField(max_length=55, blank=False, null=False)
    address = models.ForeignKey(
        Address, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='resident'
    )

    def __str__(self):
        return f'{self.id}: {self.last_name}, {self.first_name}'
