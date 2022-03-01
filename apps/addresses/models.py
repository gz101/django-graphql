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
        max_length=3, choices=STATE_CHOICES, default=STATE_CHOICES[0]
    )

    def __str__(self):
        keys = [i[0] for i in self.STATE_CHOICES]
        state_value = self.STATE_CHOICES[keys.index(self.state)][1]
        return f'{self.number} {self.street}, {self.city} {state_value}'

    @staticmethod
    def valid_state(state):
        return state in [i[0] for i in Address.STATE_CHOICES]
