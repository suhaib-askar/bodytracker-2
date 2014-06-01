from django.contrib import admin

from .models import (
    Goal, WeightEntry, DistanceActivity, RepetitionActivity, Set, ActivitySet,
    Activity
)


admin.site.register(Goal)
admin.site.register(WeightEntry)
admin.site.register(DistanceActivity)
admin.site.register(RepetitionActivity)
admin.site.register(Set)
admin.site.register(ActivitySet)
admin.site.register(Activity)
