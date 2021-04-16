from django.db import models

class Data(models.Model):
    date = models.DateField(primary_key=True)
    EC2 = models.IntegerField()
    RDS = models.IntegerField()

    def __str__(self):
        return str(self.date)
