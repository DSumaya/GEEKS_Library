from django.db import models
from django.contrib.auth.models import User

class CustomUsers(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    phone_number = models.CharField(max_length=14)
    experience = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=1, choices= GENDER)
    club = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.experience < 1:
            self.club = 'Вы нам не подходите'
        elif 1 <= self.experience < 3:
            self.club = 'Junior club 1000$'
        elif 3 <= self.experience < 7:
            self.club = 'Middle club 2000$'
        elif 5 <= self.experience <= 10:
            self.club = 'Senior club 5000$'
        else:
            self.club = 'Ваш опыт больше 10 лет'

        super().save( *args, **kwargs)


