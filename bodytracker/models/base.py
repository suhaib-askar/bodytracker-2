from django.db import models


class WeightEntry(models.Model):
    when = models.DateTimeField(
        auto_now_add=True
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    body_fat = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
    )

    class Meta:
        verbose_name_plural = 'weight entries'

    def __str__(self):
        return '{0}kg - {1}%'.format(
            self.weight, self.body_fat
        )


class Goal(models.Model):
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    body_fat = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
    )

    def __str__(self):
        return '{0}kg - {1}%'.format(
            self.weight, self.body_fat
        )
