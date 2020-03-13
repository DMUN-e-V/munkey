from django.db import models
from django.db.models import (
    CharField,
    DateField,
    CASCADE,
    ForeignKey,
    TextField,
    IntegerField,
)
from django.urls import reverse

from munkey import settings
from user_management.models import UserProfile


class Conference(models.Model):
    name = CharField(max_length=255)
    start_date = DateField()
    end_date = DateField()

    def __str__(self):
        return self.name


class Committee(models.Model):
    name = CharField(max_length=255)
    conference = ForeignKey(Conference, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Paper(models.Model):
    POSITION_PAPER = 1
    WORKING_PAPER = 2
    PRESENTATION_PAPER = 3
    PAPER_TYPES = (
        (POSITION_PAPER, "Position Paper"),
        (WORKING_PAPER, "Working Paper"),
        (PRESENTATION_PAPER, "Presentation Paper"),
    )

    user = ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="papers"
    )
    committee = ForeignKey(Committee, on_delete=CASCADE)
    type = IntegerField(choices=PAPER_TYPES)
    content = TextField()

    def __str__(self):
        return "{}: {} ({})".format(
            self.get_type_display(), self.user.get_full_name(), self.committee.name
        )

    def get_absolute_url(self):
        return reverse("paper_management:paper_detail", kwargs={"pk": self.pk})
