from django.db import models

# Create Model for Saved Stocks


class Stock(models.Model):
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol
