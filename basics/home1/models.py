from django.db import models

# Create your models here.
class details(models.Model)  :
    Username = models.CharField(max_length=122)
    Userid = models.IntegerField()
    Count = models.IntegerField(default= 0)

    def __str__(self):

        return self.Username


 