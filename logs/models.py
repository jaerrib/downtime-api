from django.conf import settings
from django.db import models


class Log(models.Model):
    customer_name = models.CharField(max_length=100)
    assembly_number = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    lot_number = models.CharField(max_length=100)
    date = models.DateField()
    shift = models.IntegerField()
    down_time = models.TimeField()
    restart_time = models.TimeField()
    problem = models.TextField()
    root_cause = models.TextField()
    corrective_action = models.TextField()
    impact = models.TextField()
    initiator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.assembly_number + "-" + self.lot_number + "-Entry" + str(
            self.pk)
