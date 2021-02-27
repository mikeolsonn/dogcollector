from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=250)
    breed = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dogs_detail', kwargs={'dog_id': self.id})

class Feeding(models.Model):
    # fields for the feeding model:
    date = models.DateField('feeding date')
    # meal will be represented as b, l or d
    meal = models.CharField(
        max_length=1, 
        choices=MEALS, 
        default=MEALS[0][0]
        )
    # one cat has many feedings
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"{self.get_meal_display()} at {self.date}"

    class Meta:
        ordering = ['-date']

