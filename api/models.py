from django.db import models

# Create your models here.
class Newletter(models.Model):
    Newsname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Newsname
    

class Item(models.Model):
    Itemname = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    newsitem = models.ForeignKey(Newletter, on_delete=models.CASCADE)


    def __str__(self):
        return self.Itemname