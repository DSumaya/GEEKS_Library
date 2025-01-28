from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT_CHOICE = (
        ('Грамм', 'Грамм'),
        ('Килограмм', 'Килограмм'),
        ('Мллилитры', 'Мллилитры' ),
        ('Литры', 'Литры'),
        ('Штуки', 'Штуки')
    )

    name = models.CharField(max_length=100, verbose_name= 'Название ингредиента')
    quantity = models.IntegerField(default=100, verbose_name= 'Количество')
    unit = models.CharField(max_length=100, choices=UNIT_CHOICE, verbose_name= 'Единица измерения')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name= 'ingredients', verbose_name= 'Рецепт')

    def __str__(self):
        return f"{self.name} {self.quantity} {self.unit}"
