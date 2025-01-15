from django.db import models

class Tag (models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Books (models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    price = models.PositiveIntegerField(default=100)


    def __str__(self):
        return self.name


