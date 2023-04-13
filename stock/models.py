from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Stock(models.Model):

    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stock-details-view', kwargs={'pk': self.id})
    