from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Bus(models.Model):

    class Meta:
        db_table = "bus"
        verbose_name = "bus"
        verbose_name_plural = "buses"

    number_plate = models.CharField(max_length=12, null=False, blank=False, unique=True)
    capacity = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(35),MaxValueValidator(55)], help_text="35 - 55")
    

    def __str__(self):
        return self.number_plate