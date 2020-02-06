from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, DateField, CASCADE, ForeignKey, OneToOneField, TextField, ManyToManyField, \
    IntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class MunkeyUser(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    birth_date = DateField()
    address = TextField()
    conference = ManyToManyField(Conference)
    committee = ManyToManyField(Committee)

    def __str__(self):
        return self.user.get_full_name()


class Paper(models.Model):
    POSITION_PAPER = 1
    WORKING_PAPER = 2
    PRESENTATION_PAPER = 3
    PAPER_TYPES = (
        (POSITION_PAPER, "Position Paper"),
        (WORKING_PAPER, "Working Paper"),
        (PRESENTATION_PAPER, "Presentation Paper"),
    )

    user = ForeignKey(User, on_delete=CASCADE)
    committee = ForeignKey(Committee, on_delete=CASCADE)
    type = IntegerField(choices=PAPER_TYPES)
    content = TextField()

    def __str__(self):
        return self.user.get_full_name() + self.committee.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MunkeyUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
