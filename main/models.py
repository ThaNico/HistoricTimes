from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class HistoricHour(models.Model):
    class Status(models.IntegerChoices):
        ON_HOLD = 0, 'On hold'
        VALID = 1, 'Valid'

    time = models.TimeField(null=False)
    year = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(2100),
            MinValueValidator(1500)
        ])
    label = models.CharField(max_length=128, null=False)
    source = models.URLField(null=False)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.ON_HOLD)

    def __str__(self):
        return '{} {} {}'.format(self.time.strftime('%H:%M'), self.year, self.label)
