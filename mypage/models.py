from django.db import models

# Create your models here.
class Dailyupdates(models.Model):
    question = models.ForeignKey(Dailyupdates, on_delete=models.CASCADE)
    Dailyupdates_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")
