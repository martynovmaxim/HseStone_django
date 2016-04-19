from django.db import models

class Player(models.Model):
    nickName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    numberOfWins = models.IntegerField()
    numberOfLose = models.IntegerField()
    #percantageOfWins = models.FloatField()
    #image = models.ImageField()

    def win(self):
        self.numberOfWins += 1
        self.save()

    def lose(self):
        self.numberOfLose += 1
        self.save()

# Create your models here.
