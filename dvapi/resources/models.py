from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from localflavor.cl.forms import CLRutField


class Drug(models.Model):
    """Drug resource. Drug code must be uniqe."""
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, help_text="unique")
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.code


def validate_rut(value):
    """
    Simple RUT validator using django-localflavor CLRutField's `clean()` method
    As oposed to FormField clean() methods's purpose. Validators should only Raise
    an Exception if validation criteria isn't met.
    """
    rut = CLRutField()
    rut.clean(value)


class Vaccination(models.Model):
    """Vaccination resource. Indicates used drug."""
    rut = models.CharField(max_length=12, validators=[validate_rut])
    dose = models.DecimalField(max_digits=3,
                               decimal_places=2,
                               validators=[
                                   MinValueValidator(0.15),
                                   MaxValueValidator(1.0),
                               ],
                               help_text="applied volume in cm3 0.15 <= dose <= 1.0")
    date = models.DateField(help_text="date of vaccination")
    drug = models.ForeignKey(Drug, on_delete=models.PROTECT)

    # def __str__(self):
    #     return F'{self.date }{self.rut}'
