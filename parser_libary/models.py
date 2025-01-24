from django.db import models
class LibraryParser(models.Model):
    description = models.CharField(max_length=100)
    href = models.URLField()

    def __str__(self):
        return self.description

