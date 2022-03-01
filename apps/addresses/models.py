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

    def valid_state(self, state):
        return state in self.STATE_CHOICES
