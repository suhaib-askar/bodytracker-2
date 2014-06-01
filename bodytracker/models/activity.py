from django.db import models


class Activity(models.Model):
    when = models.DateTimeField()
    finished = models.BooleanField(default=False)
    calories = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'activities'


class DistanceActivity(Activity):
    distance = models.PositiveIntegerField(
        help_text='Distance in meters',
        null=True,
        blank=True,
    )

    duration = models.PositiveIntegerField(
        help_text='Duration in seconds',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'distance activities'


class RepetitionActivity(Activity):
    pass

    class Meta:
        verbose_name_plural = 'repetition activities'


class Set(models.Model):

    reps = models.PositiveSmallIntegerField()

    weight = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    activity = models.ForeignKey('bodytracker.RepetitionActivity')

    class Meta:
        order_with_respect_to = 'activity'


class ActivitySet(models.Model):
    title = models.CharField(max_length=100)
    activities = models.ManyToManyField(
        'bodytracker.Activity'
    )


class ActivityDefinition(models.Model):

    title = models.CharField(max_length=100)

    activity_type = models.CharField(
        max_length=100,
        choices=[
            ('RepetitionActivity', 'Repetition'),
            ('DistanceActivity', 'Distance'),
        ]
    )
