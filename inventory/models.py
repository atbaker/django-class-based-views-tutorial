from django.core.urlresolvers import reverse
from django.db import models

class Cheese(models.Model):
    """A type of cheese in the Curd Shop inventory"""

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('view_cheese', args=[str(self.id)])
