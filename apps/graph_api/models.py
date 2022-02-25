from django.db import models


class Address(models.Model):
    number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    STATE_CHOICES = [
        ('NA', 'None Selected'),
        ('NSW', 'New South Wales'),
        ('VIC', 'Victoria'),
        ('ACT', 'Australian Captial Territory'),
        ('QLD', 'Queensland'),
        ('SA', 'South Australia'),
        ('NT', 'Northern Territory'),
        ('WA', 'Western Australia'),
        ('TAS', 'Tasmania'),
    ]
    state = models.CharField(
        max_length=3, choices=STATE_CHOICES, default='NA'
    )

    def __str__(self):
        return f'{self.number} {self.street}, {self.city} {self.state}'


class Person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=55)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, related_name='address'
    )

    def __str__(self):
        return f'{self.name}, {self.email}'
