
from datetime import datetime
from django.db import models
from rates.currencylayer import CurrencyLayer


class Currency(models.Model):
    symbol = models.CharField(max_length=3)


class Rate(models.Model):
    ccy_from = models.ForeignKey(Currency, related_name="ccy_from")
    ccy_to = models.ForeignKey(Currency, related_name="ccy_to")
    rate = models.DecimalField(max_digits=19, decimal_places=6, default=0)
    last_rate = models.DateTimeField(null=True, blank=True)
