from django.db import models

class dayofweek(models.Model):
    day_name = models.CharField(max_length=20)
    slot_1 = models.CharField(max_length=100)
    slot_2 = models.CharField(max_length=100)
    slot_3 = models.CharField(max_length=100)
    slot_4 = models.CharField(max_length=100)
    slot_5 = models.CharField(max_length=100)
    slot_6 = models.CharField(max_length=100)

    def __str__(self):
        return self.day_name
