from django.db import models


class Event(models.Model):
    class Status(models.IntegerChoices):
        ON_HOLD = 0, 'On hold'
        VALID = 1, 'Valid'

    time = models.TimeField(null=False)
    label = models.CharField(max_length=128, null=False)
    source = models.URLField(null=False)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.ON_HOLD)

    def __str__(self):
        return '{} {}'.format(self.time.strftime('%H:%M'), self.label)
